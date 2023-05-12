rm -fr example_out
./run_network.py --weights pretrained_model_weights.h5 \
                 --scene example_scene.json \
                 --output example_out \
                 --write-ply \
                 train_network_tf.py
