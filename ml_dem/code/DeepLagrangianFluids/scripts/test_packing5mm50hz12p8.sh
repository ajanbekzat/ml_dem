modelDIR="/lustre/scratch/lul/tfdata/50hzpacking5mm_data/results-1GPU-filterScale6-importance1-gamma1-12p8"
#outDIR="/lustre/scratch/lul/tfdata/TestingCases/packing_000010"
#JSON=test_packing000010.json
outDIR="/lustre/scratch/lul/tfdata/TestingCases/packing5mm_000010"
JSON=test_packing50hz5mm.json
#rm -fr ${outDIR}/runCovNet100
./mfix_run_network.py --weights ${modelDIR}/model_weights_24000.h5 \
                 --num_steps 250 \
                 --scene ${JSON} \
                 --output ${outDIR}/runCovNetfilter6-12p8\
                 --write-bgeo \
                 trainPacking5mm50hz128.py
