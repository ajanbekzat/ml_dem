modelDIR="/lustre/scratch/lul/tfdata/50hzdrum_data/results-1GPU-filterScale6-importance1-gamma1"
./evaluate_network.py --weights ${modelDIR}/model_weights_24000.h5 \
                      --trainscript trainDrum.py
