modelDIR="/lustre/scratch/lul/tfdata/50hzpacking_data/baseloss5050"
JSON=test_packing000010.json
i=50000
while [ $i -le 100000 ]
do
	outDIR="/lustre/scratch/lul/tfdata/TestingCases/packing_000010/baseloss5050_${i}"
	rm -fr ${outDIR}
	./mfix_run_network.py --weights ${modelDIR}/model_weights_${i}.h5 \
                 --num_steps 1000 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainPacking.py
	i=$(( $i + 5000 ))
done
