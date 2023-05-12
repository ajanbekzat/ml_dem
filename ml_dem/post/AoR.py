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
rc('lines', linewidth=0.4)
NF0=0
NF1=500

                      
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
        ke=0
        x0=0.5
        y0=0.5
        np=data.GetNumberOfPoints()
        for i in range(np):
            p = data.GetPoints().GetPoint(i) #p is a tuple with the x,y & z coordinates.
            vx= velList.GetValue(i*3+0)
            vy= velList.GetValue(i*3+1)
            vz= velList.GetValue(i*3+2)
            ke+= (vx*vx+vy*vy+vz*vz)
            avgx+=p[0]
            avgy+=p[1]
        avgx/=np
        avgy/=np
        dist=sqrt((avgx-x0)**2+(avgy-y0)**2)
        lx=avgx-x0
        aor = asin(lx/dist)*180/pi
        print(np,avgx,avgy,lx/dist)
    return aor,ke

aor=[]
ke=[]
time=[]
rootdir = "/lustre/scratch/lul/tfdata/TestingCases/drummew/"
dirNameList  = ["PARTIO/"]
fileNameList=[".vtp","fluid_0100.csv"]
for i in range(NF0,NF1,10):
    file = rootdir+dirNameList[0]+"PARTICLEDATA_FLUID0_{:04d}.vtp".format(i)
    iaor,ike = readVTK(file)
    aor.append(iaor)
    ke.append(ike)
    time.append((i)*0.02)

##############plot

colors = ['black', 'blue', 'maroon', 'grey']#, 'darkorange', 'bisque']
sublabel=["radial-x","radial-y","axial-z"]

rid=0
fig,axe=plt.subplots(1,1)
plt.plot(time,aor,label="MFiX")
########################## ADD SIM DATA ############
dirNameList  = ["runCovNet25casesrerun/"]
label_string = dirNameList

ncase=len(dirNameList)
saor=[]
ske=[]
for i in range(ncase):
    fileName = rootdir+dirNameList[0]+"tfResults.txt"
    data=np.loadtxt(fileName,skiprows=0, usecols = (0,1,2,3,4))
    simTime=data[:,0]*0.02
    apx = data[:,1]
    apy = data[:,2]
    ake = data[:,4]
    
    iaor=[]    
    ldata=len(apx)
    for j in range(ldata):
        dist=sqrt((apx[j]-0.5)**2+(apy[j]-0.5)**2)
        lx=apx[j]-0.5
        iiaor = asin(lx/dist)*180/pi
        iaor.append(iiaor)
    saor.append(iaor)
    ske.append(ake)
    plt.plot(simTime,iaor,label=label_string[i])
    

axe.legend(loc='lower right', prop={'size': 8})

plt.xlabel('Time (s)')
plt.ylabel('AoR (-)')
plt.savefig(rootdir+'drumAoR_{:d}.png'.format(rid))
plt.show()
plt.clf()