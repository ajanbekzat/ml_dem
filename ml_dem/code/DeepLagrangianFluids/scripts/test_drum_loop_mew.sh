modelDIR="/lustre/scratch/lul/tfdata/50hzdrummew100cases_data/baseLoseMew100"
JSON=test_drum_mew.json
i=100000
while [ $i -le 100000 ]
do
	outDIR="/lustre/scratch/lul/tfdata/TestingCases/drummew/baseLoseMew100_${i}"
	rm -fr ${outDIR}
	./mfix_run_network_mew.py --weights ${modelDIR}/model_weights_${i}.h5 \
                 --num_steps 1000 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainDrumMew.py
	i=$(( $i + 5000 ))
done
