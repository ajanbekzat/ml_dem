model="100hzbaseloss5050frames50"
modelDIR="/lustre/scratch/lul/tfdata/100hzhopper5cm_data/${model}"
#modelDIR="/lustre/scratch/lul/tfdata/50hzhopper5cm_data/${model}"
JSON=test_hopper5cm_case5.json
i=5000
while [ $i -le 10000 ]
do
	outDIR="/lustre/scratch/lul/tfdata/TestingCases/hopper5cmcase5/${model}_${i}"
	rm -fr ${outDIR}
	./mfix_run_network.py --weights ${modelDIR}/model_weights_${i}.h5 \
                 --num_steps 400 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainHopperLoss5frames100hz.py
	i=$(( $i + 1000 ))
done
