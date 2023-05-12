modelDIR="/lustre/scratch/lul/tfdata/50hzdrum_data/baseLose"
outDIR="/lustre/scratch/lul/tfdata/TestingCases/drum_high/baseLose_100000"
JSON=test_drum07.json
rm -fr ${outDIR}
./mfix_run_network.py --weights ${modelDIR}/model_weights_100000.h5 \
                 --num_steps 1000 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainDrumLose.py
