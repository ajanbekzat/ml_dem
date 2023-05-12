modelDIR="/lustre/scratch/lul/tfdata/50hzdrummew100cases_data/resultsMEW"
outDIR="/lustre/scratch/lul/tfdata/TestingCases/drummew/runCovNet100cases"
JSON=test_drum_mew.json
rm -fr ${outDIR}
./mfix_run_network_mew.py --weights ${modelDIR}/model_weights.h5 \
                 --num_steps 1000 \
                 --scene ${JSON} \
                 --output ${outDIR} \
                 --write-bgeo \
                 trainDrumMew100cases.py
