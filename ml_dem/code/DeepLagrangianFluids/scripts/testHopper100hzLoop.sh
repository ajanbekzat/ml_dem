model="100hzbaseloss5050frames50"
modelDIR="/lustre/scratch/lul/tfdata/100hzhopper5cm_data/${model}"
#modelDIR="/lustre/scratch/lul/tfdata/50hzhopper5cm_data/${model}"
JSON=test_hopper5cm.json
i=10000
while [ $i -le 10000 ]
do
	outDIR="/lustre/scratch/lul/tfdata/TestingCases/hopper5cm/${model}_${i}"
	rm -fr ${outDIR}
	./mfix_run_network100hz.py --weights ${modelDIR}/model_weights_${i}.h5 \
                 --num_steps 800 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainHopperLoss5frames100hz.py
	i=$(( $i + 1000 ))
done
