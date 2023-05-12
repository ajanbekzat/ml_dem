# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from math import pi
import vtk
import os
import sys
import csv
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['DejaVu Sans'],'size':8})
rc('mathtext',**{'default':'regular'})
rc('savefig', dpi=300)
rc('figure', figsize=(4,3),dpi=300)
rc('figure', autolayout=True)
rc('legend', numpoints=1)
rc('lines', linewidth=0.4)
NF0=899
NF1=899
NFS=NF1-NF0+1


def readCSV(fileName):
    res=[[] for i in range(4)]
    with open(fileName) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for skip in range(1):
            next(readCSV)        
        for row in readCSV:
            vx=float(row[0])
            vy=float(row[1])
            vz=float(row[2])
            vm= sqrt(vx*vx+vy*vy+vz*vz)
            res[0].append(vx)
            res[1].append(vy)
            res[2].append(vz)
            res[3].append(vm)
    return res
                      
def readVTK(fname):
    res=[[] for i in range(4)]
    # create reader
    points = vtk.vtkXMLPolyDataReader()
    # loop over all vtp files
    #for fname in sorted(glob.glob(os.path.join(fdir, '*.vtp'))):
    for i in range(NF0,NF1+1):
        #fname=fdir+'PARTICLES_{:04d}.vtp'.format(i)
        print('Reading:', fname)
        points.SetFileName(fname)
        points.Update()
        # print the arrays
        data = points.GetOutput()
        point_data = data.GetPointData()

        # loop over all data arrays
        for i in range(point_data.GetNumberOfArrays()):
            if(point_data.GetArrayName(i)=='Velocity'):
                velList=point_data.GetArray(i)

        #get xyz
        for i in range(data.GetNumberOfPoints()):
            #p = data.GetPoints().GetPoint(i) #p is a tuple with the x,y & z coordinates.
            vx= velList.GetValue(i*3+0)
            vy= velList.GetValue(i*3+1)
            vz= velList.GetValue(i*3+2)
            vm= sqrt(vx*vx+vy*vy+vz*vz)
            res[0].append(vx)
            res[1].append(vy)
            res[2].append(vz)
            res[3].append(vm)
    return res


rootdir = "/lustre/scratch/lul/tfdata/TestingCases/drum1/"
dirNameList  = ["PARTIO/","runCovNet/"]
fileNameList=["PARTICLEDATA_FLUID0_0100.vtp","fluid_0100.csv"]

#dirNameList  = ["PARTIO/","PARTIO/"]
#fileNameList=["PARTICLEDATA_FLUID0_0999.vtp","PARTICLEDATA_FLUID0_0950.vtp"]
ncase=len(dirNameList)


label_string = ["MFiX","TensowFlow"]#"Dp={:4.3f} mm\nAvg. Temp={:4.2f} K"
colors = ['black', 'blue', 'maroon', 'grey']#, 'darkorange', 'bisque']
sublabel=["radial-x","radial-y","axial-z"]

rid=0
fig,axe=plt.subplots(1,1)

for i in range(ncase):
    print(i)
    dirName = dirNameList[i]
    file = rootdir+dirName+fileNameList[i]
    if i==0:
        res4=readVTK(file)
    else:
        res4=readCSV(file)
        
    res=res4[rid]
    b0=min(res)
    b1=max(res)
    bins = np.arange(b0,b1,0.01)
    lenrt=len(res)
    avg_rt=sum(res)/lenrt
    fls = label_string[i] +"("+sublabel[rid]+")" #+ "(avg={:4.2f} m/s)".format(avg_rt)
    #ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)
    axe.hist(res,bins=bins,density=True,histtype='step',stacked=False,color=colors[i], label=fls)
    #plt.plot(rt,bins=bins,density=True,fill=False,label=fls)


axe.legend(loc='upper left', prop={'size': 8})

plt.xlabel('Velocity (m/s)')
plt.ylabel('Fraction (-)')
plt.savefig(rootdir+'drumVp_{:d}.png'.format(rid))
plt.show()
plt.clf()