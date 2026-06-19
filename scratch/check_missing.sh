#!/bin/bash
cat scratch/all_images.txt scratch/all_videos.txt > scratch/all_assets.txt
comm -13 <(sort scratch/all_assets.txt) scratch/used_basenames.txt > scratch/missing_assets.txt
echo "Missing Assets:"
cat scratch/missing_assets.txt
