modelDIR="/lustre/scratch/lul/tfdata/50hzpacking_data/results-1GPU-filterScale4-importance1-gamma1-8layers"
#outDIR="/lustre/scratch/lul/tfdata/TestingCases/packing_000010"
#JSON=test_packing000010.json
outDIR="/lustre/scratch/lul/tfdata/TestingCases/packing5cmd5m"
JSON=test_packing5cmd5m.json
#rm -fr ${outDIR}/runCovNet100
./mfix_run_network.py --weights ${modelDIR}/model_weights.h5 \
                 --num_steps 250 \
                 --scene ${JSON} \
                 --output ${outDIR}/runCovNetfilter4-8layers\
                 --write-bgeo \
                 trainPacking5cm8layers.py
