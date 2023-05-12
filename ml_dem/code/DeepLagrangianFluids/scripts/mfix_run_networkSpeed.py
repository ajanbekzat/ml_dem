#!/usr/bin/env python3
import os
import sys
import argparse
import numpy as np
import re
import vtk
from glob import glob
import time
import importlib
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'datasets'))
from physics_data_helper import numpy_from_bgeo, write_bgeo_from_numpy
from create_physics_scenes import obj_surface_to_particles, obj_volume_to_particles
from create_physics_records_mfix import stl_to_particles

import open3d as o3d

def mfix_read_particles(file):
    try:
        lid=0
        n=0
        #get particle count
        with open(file) as f:
            for line in f:
                lid+=1
                if(lid==20):
                    tmp,n=line.split()
                    n=int(n)
                    break              
        pos_arr = np.empty((n, 3))
        #vel_arr = np.empty((n, 3))
        #get particle pos
        lid=0
        with open(file) as f:
            for line in f:
                lid+=1
                if(lid>=35):                   
                    x, y, z = line.split()
                    x = float(x)
                    y = float(y)
                    z = float(z)
                    pos_arr[lid-35]=[x,y,z]
                    #print("n={:d}, pid={:d} pos={:}",n,lid-35,pos_arr[lid-35])
    except IOError:
        print("Cannot open file")
        sys.exit(1)
    return pos_arr

def mfix_read_particles_from_vtk(path):
    
    # create reader
    points = vtk.vtkXMLPolyDataReader()
    points.SetFileName(path)
    points.Update()
    # print the arrays
    data = points.GetOutput()
    n = data.GetNumberOfPoints()
    pos_arr = np.empty((n, 3))  
    #get xyz
    for i in range(n):
        p = data.GetPoints().GetPoint(i) #p is a tuple with the x,y & z coordinates.
        pos_arr[i] = p

    print("particle input={:} np={:d}".format(path,n))
    return pos_arr



def write_particles(path_without_ext, pos, vel=None, options=None):
    """Writes the particles as point cloud ply.
    Optionally writes particles as bgeo which also supports velocities.
    """
    arrs = {'pos': pos}
    if not vel is None:
        arrs['vel'] = vel
    np.savez(path_without_ext + '.npz', **arrs)

    if options and options.write_ply:
        pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(pos))
        o3d.io.write_point_cloud(path_without_ext + '.ply', pcd)

    if options and options.write_bgeo:
        write_bgeo_from_numpy(path_without_ext + '.bgeo', pos, vel)


def run_sim_tf(trainscript_module, weights_path, scene, num_steps, output_dir,
               options):

    # init the network
    model = trainscript_module.create_model()
    model.init()
    model.load_weights(weights_path, by_name=True)

    # prepare static particles
    walls = []
    for x in scene['walls']:
        #points, normals = obj_surface_to_particles(x['path'])
        points, normals = stl_to_particles(x['path'])
        if 'invert_normals' in x and x['invert_normals']:
            normals = -normals
        points += np.asarray([x['translation']], dtype=np.float32)
        walls.append((points, normals))
    box = np.concatenate([x[0] for x in walls], axis=0)
    box_normals = np.concatenate([x[1] for x in walls], axis=0)

    # export static particles
    write_particles(os.path.join(output_dir, 'box'), box, box_normals, options)

    # compute lowest point for removing out of bounds particles
    min_y = np.min(box[:, 1]) - 0.05 * (np.max(box[:, 1]) - np.min(box[:, 1]))

    # prepare fluids
    fluids = []
    for x in scene['fluids']:
        #points = obj_volume_to_particles(x['path'])[0]
        points = mfix_read_particles_from_vtk(x['path'])
       # points += np.asarray([x['translation']], dtype=np.float32)
        velocities = np.empty_like(points)
        velocities[:, 0] = x['velocity'][0]
        velocities[:, 1] = x['velocity'][1]
        velocities[:, 2] = x['velocity'][2]
        range_ = range(x['start'], x['stop'], x['step'])
        fluids.append((points, velocities, range_))

    pos = np.empty(shape=(0, 3), dtype=np.float32)
    vel = np.empty_like(pos)

    model.summary()
    
    #######################
    fileName=os.path.join(output_dir,'tfResults.txt')
    resFile = open(fileName,"w")
    
    startTime=time.time()
    for step in range(num_steps):
        # add from fluids to pos vel arrays
        for points, velocities, range_ in fluids:
            if step in range_:  # check if we have to add the fluid at this point in time
                pos = np.concatenate([pos, points], axis=0)
                vel = np.concatenate([vel, velocities], axis=0)

        if pos.shape[0]:
            fluid_output_path = os.path.join(output_dir,
                                             'fluid_{0:04d}'.format(step))
            if isinstance(pos, np.ndarray):
                write_particles(fluid_output_path, pos, vel, options)
            else:
                write_particles(fluid_output_path, pos.numpy(), vel.numpy(),
                                options)

            inputs = (pos, vel, None, box, box_normals)
            pos, vel = model(inputs)

        # remove out of bounds particles
        if step < 0:
            ########################
            #write centroid of the particle bed, which reflects AoR, see https://doi.org/10.1016/j.ces.2020.116251
            pc = np.average(pos,axis=0)
            avgVel = np.average(vel,axis=0)
            gt = np.sum((vel-avgVel)**2,axis=0)/pos.shape[0]
            #ke = np.sum(vel**2)
            #for iv in vel:
            #    ke+=(iv[0]*iv[0] + iv[1]*iv[1] +iv[2]*iv[2])
            resFile.write("{:d} {:f} {:f} {:f} {:f} {:f} {:f}\n".format(step,pc[0],pc[1],pc[2],gt[0],gt[1],gt[2])) 
            print("step={:d} pos={:f} {:f} {:f} v2={:f} {:f} {:f}\n".format(step,pc[0],pc[1],pc[2],gt[0],gt[1],gt[2])) 
            
            print(step, 'num particles', pos.shape[0])
            mask = pos[:, 1] > min_y
            if np.count_nonzero(mask) < pos.shape[0]:
                pos = pos[mask]
                vel = vel[mask]
    print("Total time = {:.2f} s".format(time.time()-startTime))
def main():
    parser = argparse.ArgumentParser(
        description=
        "Runs a fluid network on the given scene and saves the particle positions as npz sequence",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("trainscript",
                        type=str,
                        help="The python training script.")
    parser.add_argument(
        "--weights",
        type=str,
        required=True,
        help=
        "The path to the .h5 network weights file for tensorflow ot the .pt weights file for torch."
    )
    parser.add_argument("--num_steps",
                        type=int,
                        default=250,
                        help="The number of simulation steps. Default is 250.")
    parser.add_argument("--scene",
                        type=str,
                        required=True,
                        help="A json file which describes the scene.")
    parser.add_argument("--output",
                        type=str,
                        required=True,
                        help="The output directory for the particle data.")
    parser.add_argument("--write-ply",
                        action='store_true',
                        help="Export particle data also as .ply sequence")
    parser.add_argument("--write-bgeo",
                        action='store_true',
                        help="Export particle data also as .bgeo sequence")
    parser.add_argument("--device",
                        type=str,
                        default='cuda',
                        help="The device to use. Applies only for torch.")

    args = parser.parse_args()
    print(args)

    module_name = os.path.splitext(os.path.basename(args.trainscript))[0]
    sys.path.append('.')
    trainscript_module = importlib.import_module(module_name)

    with open(args.scene, 'r') as f:
        scene = json.load(f)

    os.makedirs(args.output)

    if args.weights.endswith('.h5'):
        return run_sim_tf(trainscript_module, args.weights, scene,
                          args.num_steps, args.output, args)
    elif args.weights.endswith('.pt'):
        return run_sim_torch(trainscript_module, args.weights, scene,
                             args.num_steps, args.output, args)


if __name__ == '__main__':
    sys.exit(main())
