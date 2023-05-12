def mfix_numpy_from_bgeo(path):
    # create reader
    points = vtk.vtkXMLPolyDataReader()
    points.SetFileName(path)
    points.Update()
    # print the arrays
    data = points.GetOutput()
    point_data = data.GetPointData()
    n = data.GetNumberOfPoints()
    pos_arr = np.empty((n, 3))
    vel_arr = np.empty((n, 3))
    rho_arr = np.empty((n))
    # loop over all data arrays
    
#											UNCOMMENT THESE LINES IF DATA IS FROM MFIX
    # for i in range(point_data.GetNumberOfArrays()):
    #     if(point_data.GetArrayName(i)=='Density'):
    #         rou=point_data.GetArray(i)
    #     if(point_data.GetArrayName(i)=='Velocity'):
    #         vel=point_data.GetArray(i)

#										      UNCOMMENT THESE LINES IF DATA IS FROM ASPHERIX        
    for i in range(point_data.GetNumberOfArrays()):
        if(point_data.GetArrayName(i)=='density'):
            rou=point_data.GetArray(i)
        if(point_data.GetArrayName(i)=='v'):
            vel=point_data.GetArray(i)
  
    #get xyz 					
    for i in range(n):
        p = data.GetPoints().GetPoint(i) #p is a tuple with the x,y & z coordinates.
        v = [vel.GetValue(3*i),vel.GetValue(3*i+1),vel.GetValue(3*i+2)]
        rho = rou.GetValue(i)
        pos_arr[i] = p
        vel_arr[i] = v
        rho_arr[i] = rho

        #if i==0:
        #    print(p,v,rho)

    result = [pos_arr, vel_arr, rho_arr]
    return tuple(result)
