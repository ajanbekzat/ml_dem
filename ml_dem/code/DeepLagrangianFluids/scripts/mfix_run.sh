caseDIR="/lustre/scratch/lul/tfdata/50hzpacking5mm_data/results-1GPU-filterScale6-importance1-gamma1"
JSON=mfix_scene_packing.json
#caseDIR="/lustre/scratch/lul/tfdata/50hzdrum_data/results-1GPU-filterScale6-importance1-gamma1"
rm -fr ${caseDIR}/run
#./mfix_run_network.py --weights ./mfix_train_network_tf/model_weights.h5 \
#./mfix_run_network.py --weights ./pretrained_model_weights.h5 \
#./mfix_run_network.py --weights /lustre/scratch/lul/tfdata/1khz_data/results-1GPU/model_weights.h5 \
./mfix_run_network.py --weights ${caseDIR}/model_weights_24000.h5 \
                 --num_steps 2000 \
                 --scene ${JSON} \
                 --output ${caseDIR}/run\
                 --write-ply \
                 mfix_train_network_tfDMP.py
