#!/bin/bash

# Set the path to SPlishSPlasHs DynamicBoundarySimulator in splishsplash_config.py
# before running this script

# output directories
#OUTPUT_SCENES_DIR="/nfs/home/6/lul/tf/DeepLagrangianFluid/mfix/mfixOutput"
#OUTPUT_SCENES_DIR="/lustre/scratch/lul/tfdata/1khz"
#OUTPUT_DATA_DIR="/lustre/scratch/lul/tfdata/1khz_data"
OUTPUT_SCENES_DIR="/lustre/scratch/lul/tfdata/100hzhopper5cm"
OUTPUT_DATA_DIR="$OUTPUT_SCENES_DIR""_data"

rm -fr $OUTPUT_DATA_DIR

# Transforms and compresses the data such that it can be used for training.
# This will also create the OUTPUT_DATA_DIR.
python create_physics_records_mfix.py --input $OUTPUT_SCENES_DIR  --output $OUTPUT_DATA_DIR  
#python create_physics_records_mfix_mew.py --input $OUTPUT_SCENES_DIR  --output $OUTPUT_DATA_DIR  
