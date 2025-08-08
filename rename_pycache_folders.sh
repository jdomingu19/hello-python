#!/bin/bash

# Change to the Board of Directors
cd "d:/Jesús/Documentos/hello-python/cuc-old/" || exit 1

# Find all the folders called -pycache-and rename __pycache__
find . -type d -name "-pycache-" | while read -r dir; do
  parent=$(dirname "$dir")
  newdir="$parent/__pycache__"
  echo "renamed: $dir → $newdir"
  mv "$dir" "$newdir"
done
