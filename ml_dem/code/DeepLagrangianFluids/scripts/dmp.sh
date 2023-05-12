#doesn't ivoke mpi proceees
#mpirun -np 2  -bind-to none  python mfix_train_network_tfDMP.py
#sleep 1h
#mv /lustre/scratch/lul/tfdata/500hz5cm1geo_data/*.zst /lustre/scratch/lul/tfdata/500hz5cm1geo_data/train/
#connection refused
horovodrun -np 2  python mfix_train_network_tfDMP_wall.py
#python mfix_train_network_tfDMP0108.py
#horovodrun -np 4 python mfix_train_network_tfDMP4.py
#horovodrun -np 6 -H n846:2,n852:2,n848:2 python mfix_train_network_tfDMP4.py


#horovodrun -np 2 python mfix_train_network_tfDMP.py
