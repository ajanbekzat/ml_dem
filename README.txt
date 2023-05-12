Data from MFIX-DEM and Aspherix solvers are in their respective folders in the PARTIO directory
.vtp files are binary. 
MFIX-DEM .vtp files contain information about particle's "Velocity", "Density", "Diameter" 
Aspherix .vtp files contain information about particle's "id", "v", "f", "density", "radius", "mass".  "v" stands for velocity and "f" for force 
Data of a particular instance can be read using the vtk library with a label provided. Labels are given in "" as above. 
pip install vtk - to install the library  
An example code function of data transformation from vtk to numpy array is provided in the vtk_to_np_array.py file  
