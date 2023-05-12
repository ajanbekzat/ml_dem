modelDIR="/lustre/scratch/lul/tfdata/50hzdrumfit_data/basek100"
outDIR="/lustre/scratch/lul/tfdata/TestingCases/drum1/fitbasek100_8000"
JSON=test_drum.json
rm -fr ${outDIR}
./mfix_run_network.py --weights ${modelDIR}/model_weights_8000.h5 \
                 --num_steps 1000 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainDrumFitbasek100.py
