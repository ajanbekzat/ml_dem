modelDIR="/lustre/scratch/lul/tfdata/50hzdrumfit_data/basek100LoseBatch32gpu2"
JSON=test_drum.json
i=5000
while [ $i -le 24000 ]
do
	outDIR="/lustre/scratch/lul/tfdata/TestingCases/drum1/fitbaseLoseBatch32gpu2_${i}"
	rm -fr ${outDIR}
	./mfix_run_network.py --weights ${modelDIR}/model_weights_${i}.h5 \
                 --num_steps 1000 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainDrumFitbasek100Loss.py
	i=$(( $i + 1000 ))
done
