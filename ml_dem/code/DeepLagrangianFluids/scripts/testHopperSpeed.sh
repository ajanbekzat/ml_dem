model="baseloss5050frames3w127k2000"
modelDIR="/lustre/scratch/lul/tfdata/50hzhopper5cm_data/${model}"
#modelDIR="/lustre/scratch/lul/tfdata/50hzhopper5cm_data/${model}"
JSON=test_hopper5cm.json
i=100000
while [ $i -le 100000 ]
do
	outDIR="/lustre/scratch/lul/tfdata/TestingCases/hopper5cm/${model}_${i}"
	rm -fr ${outDIR}
	./mfix_run_networkSpeed.py --weights ${modelDIR}/model_weights_${i}.h5 \
                 --num_steps 400 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainHopperLoss.py
	i=$(( $i + 10000 ))
done
