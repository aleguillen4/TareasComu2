#!/bin/bash

# Redirect all output to log.txt file
exec &> log.txt

# Loop through all files in misc folder with .tiff extension
for file in misc/*.tiff; do
  echo "Running command: python3 base5.py -i $file"
  python3 base5.py -i "$file"
done
