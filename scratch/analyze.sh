#!/bin/bash

echo "--- Images ---"
ls -1 assets/images > scratch/all_images.txt
cat scratch/all_images.txt

echo "--- Videos ---"
ls -1 assets/videos > scratch/all_videos.txt
cat scratch/all_videos.txt

echo "--- References in index.html ---"
grep -oE '(assets/images/[^"'\''\>]+|assets/videos/[^"'\''\>]+)' index.html | sort | uniq > scratch/used_main.txt
cat scratch/used_main.txt

echo "--- References in piano-editoriale/index.html ---"
grep -oE '(\.\./assets/images/[^"'\''\>]+|\.\./assets/videos/[^"'\''\>]+)' piano-editoriale/index.html | sort | uniq > scratch/used_piano.txt
cat scratch/used_piano.txt
