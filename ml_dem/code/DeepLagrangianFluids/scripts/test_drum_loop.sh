modelDIR="/lustre/scratch/lul/tfdata/50hzdrum_data/baseLose3"
JSON=test_drum.json
i=50000
while [ $i -le 100000 ]
do
	outDIR="/lustre/scratch/lul/tfdata/TestingCases/drum1/baseLose3_${i}"
	rm -fr ${outDIR}
	./mfix_run_network.py --weights ${modelDIR}/model_weights_${i}.h5 \
                 --num_steps 1000 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainDrum2.py
	i=$(( $i + 5000 ))
done
