modelDIR="/lustre/scratch/lul/tfdata/50hzdrumfit_data/basek100LoseNormal"
JSON=test_drum.json
i=5000
while [ $i -le 24000 ]
do
	outDIR="/lustre/scratch/lul/tfdata/TestingCases/drum1/fitbaseLoseNormal_${i}"
	rm -fr ${outDIR}
	./mfix_run_network.py --weights ${modelDIR}/model_weights_${i}.h5 \
                 --num_steps 1000 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainDrumFitbasek100LossNormal.py
	i=$(( $i + 1000 ))
done
