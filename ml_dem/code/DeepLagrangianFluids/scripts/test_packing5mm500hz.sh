modelDIR="/lustre/scratch/lul/tfdata/500hzpacking5mm_data/results-1GPU-filterScale6-importance1-gamma1"
#outDIR="/lustre/scratch/lul/tfdata/TestingCases/packing_000010"
#JSON=test_packing000010.json
outDIR="/lustre/scratch/lul/tfdata/TestingCases/packing5mm500hz_000010"
JSON=test_packing500hz5mm.json
#rm -fr ${outDIR}/runCovNet100
./mfix_run_network.py --weights ${modelDIR}/model_weights_24000.h5 \
                 --num_steps 2500 \
                 --scene ${JSON} \
                 --output ${outDIR}/runCovNetfilter6\
                 --write-bgeo \
                 trainPacking5mm500hz.py
