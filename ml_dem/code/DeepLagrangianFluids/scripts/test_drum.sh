modelDIR="/lustre/scratch/lul/tfdata/50hzdrum_data/base"
outDIR="/lustre/scratch/lul/tfdata/TestingCases/drum1/base_45000"
JSON=test_drum.json
rm -fr ${outDIR}
./mfix_run_network.py --weights ${modelDIR}/model_weights_45000.h5 \
                 --num_steps 1000 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainDrum2.py
