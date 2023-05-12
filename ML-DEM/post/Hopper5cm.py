# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from math import pi
import vtk
import os
import sys
import csv
import numpy as np
from math import sqrt,asin,pi
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['DejaVu Sans'],'size':8})
rc('mathtext',**{'default':'regular'})
rc('savefig', dpi=300)
rc('figure', figsize=(4,3),dpi=300)
rc('figure', autolayout=True)
rc('legend', numpoints=1)
rc('lines', linewidth=0.8)
NF0=0
NF1=200

                      
def readVTK(fname):
    res=[[] for i in range(4)]
    # create reader
    points = vtk.vtkXMLPolyDataReader()
    # loop over all vtp files
    #for fname in sorted(glob.glob(os.path.join(fdir, '*.vtp'))):
    for j in range(1):
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
        avgx=0
        avgy=0
        u=[]
        v=[]
        w=[]
        ke=0
        x0=0.5
        y0=0.5
        npart=data.GetNumberOfPoints()
        for i in range(npart):
            p = data.GetPoints().GetPoint(i) #p is a tuple with the x,y & z coordinates.
            vx= velList.GetValue(i*3+0)
            vy= velList.GetValue(i*3+1)
            vz= velList.GetValue(i*3+2)
            u.append(vx)
            v.append(vy)
            w.append(vz)
            avgx+=p[0]
            avgy+=p[1]
        avgx/=npart
        avgy/=npart
        dist=sqrt((avgx-x0)**2+(avgy-y0)**2)
        lx=avgx-x0
        aor = avgy #asin(lx/dist)*180/pi
        
        mu = sum(u)/npart
        mv = sum(v)/npart
        mw = sum(w)/npart
        gtu=0
        gtv=0
        gtw=0
        for i in range(npart):
            gtu += ((mu-u[i])**2  )
            gtv += (mv-v[i])**2
            gtw += (mw-w[i])**2
        gtu/=npart
        gtv/=npart
        gtw/=npart
        #########check
        vel=np.zeros((npart,3))
        for i in range(npart):
            vel[i][0] = u[i]
            vel[i][1] = v[i]
            vel[i][2] = w[i]
        avgVel = np.average(vel,axis=0)
        gt2 = np.sum((vel-avgVel)**2,axis=0)/npart
        if abs(gtu/gt2[0]-1)>0.01:
            exit(-1)
        else:
            print('===============================')
            print(gtu,gtv,gtw,gt2)
        print(npart,avgx,avgy,lx/dist)
    return aor,gtu,gtv,gtw

aor=[]
ke=[]
time=[]
rootdir = "/lustre/scratch/lul/tfdata/TestingCases/hopper5cm/"
dirNameList  = ["PARTIO/"]
fileNameList=[".vtp","fluid_0100.csv"]
for i in range(NF0,NF1,10):
    file = rootdir+dirNameList[0]+"PARTICLEDATA_FLUID0_{:04d}.vtp".format(i)
    iaor,gtu, gtv, gtw = readVTK(file)
    aor.append(iaor)
    ke.append((gtu+gtv+gtw)/3)
    time.append((i)*0.02)

##############plot

colors = ['black', 'blue', 'maroon', 'grey']#, 'darkorange', 'bisque']
sublabel=["radial-x","radial-y","axial-z"]
nd=len(aor)
AVS=nd//2
avgExpAOR = sum(aor[-AVS:])/AVS
avgExpKE = sum(ke[-AVS:])/AVS
rid=0
fig,axe=plt.subplots(1,1)
plt.plot(time,aor,'-o',color='black',label="MFiX ({:.2f})".format(avgExpAOR))
########################## ADD SIM DATA ############

ncase=1#len(dirNameList)

baseAOR=[]
baseSteps=[]
baseKE=[]
baseAVGKE=[]
for i in range(ncase):
    nsteps=i*1000+10000
    fileName = rootdir+"base_{:d}/tfResults.txt".format(nsteps)
#    fileName = rootdir+dirNameList[i]+"/tfResults.txt"
    data=np.loadtxt(fileName,skiprows=0, usecols = (0,1,2,3,4,5,6))
    simTime=data[:,0]*0.02
    apx = data[:,1]
    apy = data[:,2]
    ake = (data[:,4] + data[:,5] + data[:,6])/3
    
    saor=[]   
    ske=[]
    ldata=len(simTime)
    for j in range(ldata):
        dist=sqrt((apx[j]-0.5)**2+(apy[j]-0.5)**2)
        lx=apx[j]-0.5
        iiaor = apy[j]#asin(lx/dist)*180/pi
        saor.append(iiaor)

    avgAOR = sum(saor[-AVS:])/AVS
    avgke = sum(ake[-AVS:])/AVS
    baseAOR.append(avgAOR)
    baseSteps.append(nsteps//1000)
    baseAVGKE.append(avgke)
    baseKE.append(ake)
    plt.plot(simTime,saor,'--',label="Loss (100%-0%)")
    

#exit(-1)
############################## LOSE  ##############
############################## LOSE  ##############
############################## LOSE  ##############
############################## LOSE  ##############
############################## LOSE  ##############
baseLoseAOR=[]
baseLoseKE=[]
baseLoseAVGKE=[]
#fig,axe=plt.subplots(1,1)
#plt.plot(time,aor,'-o',color='black',label="MFiX ({:.2f})".format(avgExpAOR))
for i in range(ncase):
    nsteps=i*1000+10000
    fileName = rootdir+"baseLoss5050_{:d}/tfResults.txt".format(nsteps)
#    fileName = rootdir+dirNameList[i]+"/tfResults.txt"
    data=np.loadtxt(fileName,skiprows=0, usecols = (0,1,2,3,4,5,6))
    simTime=data[:,0]*0.02
    apx = data[:,1]
    apy = data[:,2]
    ake = (data[:,4] + data[:,5] + data[:,6])/3
    
    saor=[]   
    ske=[]
    ldata=len(simTime)
    for j in range(ldata):
        dist=sqrt((apx[j]-0.5)**2+(apy[j]-0.5)**2)
        lx=apx[j]-0.5
        iiaor = apy[j]#asin(lx/dist)*180/pi
        saor.append(iiaor)
        
    avgke = sum(ake[-AVS:])/AVS    
    baseLoseAVGKE.append(avgke)
    baseLoseKE.append(ake)
    avgAOR = sum(saor[-AVS:])/AVS
    baseLoseAOR.append(avgAOR)
    plt.plot(simTime,saor,label="Loss (50%-50%)")

#########################################
for i in range(ncase):
    nsteps=i*1000+10000
    fileName = rootdir+"baseloss2080_{:d}/tfResults.txt".format(nsteps)
    data=np.loadtxt(fileName,skiprows=0, usecols = (0,1,2,3,4,5,6))
    simTime=data[:,0]*0.02
    apy = data[:,2]    
    saor=[]   
    ldata=len(simTime)
    for j in range(ldata):
        iiaor = apy[j]
        saor.append(iiaor)
        
    plt.plot(simTime,saor,'-.',label="Loss (20%-80%)")    
#####################################################

#########################################
for i in range(ncase):
    nsteps=i*1000+10000
    fileName = rootdir+"baseloss5050frames3_{:d}/tfResults.txt".format(nsteps)
    data=np.loadtxt(fileName,skiprows=0, usecols = (0,1,2,3,4,5,6))
    simTime=data[:,0]*0.02
    apy = data[:,2]    
    saor=[]   
    ldata=len(simTime)
    for j in range(ldata):
        iiaor = apy[j]
        saor.append(iiaor)        
    plt.plot(simTime,saor,'-',label="Loss (50%-50%), 3 frames")    
#####################################################
#########################################
for i in range(ncase):
    nsteps=i*1000+10000
    fileName = rootdir+"baseloss5050frames3w127_{:d}/tfResults.txt".format(nsteps)
    data=np.loadtxt(fileName,skiprows=0, usecols = (0,1,2,3,4,5,6))
    simTime=data[:,0]*0.02
    apy = data[:,2]    
    saor=[]   
    ldata=len(simTime)
    for j in range(ldata):
        iiaor = apy[j]
        saor.append(iiaor)        
    plt.plot(simTime,saor,'-',label="Loss (50%-50%), 3 frames127")    
#####################################################
#########################################
for i in range(ncase):
    nsteps=i*1000+25000
    fileName = rootdir+"baseloss5050frames3w127k2000_{:d}/tfResults.txt".format(nsteps)
    data=np.loadtxt(fileName,skiprows=0, usecols = (0,1,2,3,4,5,6))
    simTime=data[:,0]*0.02
    apy = data[:,2]    
    saor=[]   
    ldata=len(simTime)
    for j in range(ldata):
        iiaor = apy[j]
        saor.append(iiaor)        
    plt.plot(simTime,saor,'-',label="Loss (50%-50%), 3 frames127k2000")    
#####################################################
#########################################
for i in range(ncase):
    nsteps=i*1000+10000
    fileName = rootdir+"baseloss5050frames5_{:d}/tfResults.txt".format(nsteps)
    data=np.loadtxt(fileName,skiprows=0, usecols = (0,1,2,3,4,5,6))
    simTime=data[:,0]*0.02
    apy = data[:,2]    
    saor=[]   
    ldata=len(simTime)
    for j in range(ldata):
        iiaor = apy[j]
        saor.append(iiaor)        
    plt.plot(simTime,saor,'-',label="Loss (50%-50%), 5 frames")    
#####################################################
#########################################
for i in range(ncase):
    nsteps=i*1000+10000
    fileName = rootdir+"baseloss5050f200_{:d}/tfResults.txt".format(nsteps)
    data=np.loadtxt(fileName,skiprows=0, usecols = (0,1,2,3,4,5,6))
    simTime=data[:,0]*0.02
    apy = data[:,2]    
    saor=[]   
    ldata=len(simTime)
    for j in range(ldata):
        iiaor = apy[j]
        saor.append(iiaor)        
    plt.plot(simTime,saor,'--',label="Loss (50%-50%), f200")    
#####################################################
#########################################
for i in range(ncase):
    nsteps=i*1000+5000
    fileName = rootdir+"baseloss5050f200b64_{:d}/tfResults.txt".format(nsteps)
    data=np.loadtxt(fileName,skiprows=0, usecols = (0,1,2,3,4,5,6))
    simTime=data[:,0]*0.02
    apy = data[:,2]    
    saor=[]   
    ldata=len(simTime)
    for j in range(ldata):
        iiaor = apy[j]
        saor.append(iiaor)        
    plt.plot(simTime,saor,'--',label="Loss (50%-50%), f200b64")    
#####################################################
axe.legend(ncol=2,loc='upper right', prop={'size': 6})
plt.xlabel('Time (s)')
plt.ylabel('Weight center (m)')
plt.ylim(0.5,1.5)
plt.xlim(0.5,1.5)
plt.savefig(rootdir+'hopperloss{:d}.png'.format(rid))
plt.show()
plt.clf()

