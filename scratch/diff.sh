#!/bin/bash
# Extract basenames of used files
cat scratch/used_main.txt scratch/used_piano.txt | awk -F'/' '{print $NF}' | sort | uniq > scratch/used_basenames.txt

# Images difference
comm -23 <(sort scratch/all_images.txt) scratch/used_basenames.txt > scratch/unused_images.txt

# Videos difference
comm -23 <(sort scratch/all_videos.txt) scratch/used_basenames.txt > scratch/unused_videos.txt

echo "Unused Images:"
cat scratch/unused_images.txt
echo "Unused Videos:"
cat scratch/unused_videos.txt
