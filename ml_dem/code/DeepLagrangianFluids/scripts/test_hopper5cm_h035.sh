model="baseloss5050frames5"
modelDIR="/lustre/scratch/lul/tfdata/50hzhopper5cm_data/${model}"
#modelDIR="/lustre/scratch/lul/tfdata/50hzhopper5cm_data/${model}"
JSON=test_hopper5cm_h035.json
i=10000
while [ $i -le 10000 ]
do
	outDIR="/lustre/scratch/lul/tfdata/TestingCases/hopper_h035/${model}_${i}"
	rm -fr ${outDIR}
	./mfix_run_network.py --weights ${modelDIR}/model_weights_${i}.h5 \
                 --num_steps 400 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainHopperLoss.py
	i=$(( $i + 10000 ))
done
