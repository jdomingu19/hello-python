#!/bin/bash

# Change to the Board of Directors
cd "d:/Jesús/Documentos/hello-python/" || exit 1

# Find all folders (recursive), order the highest to lower depth
find . -type d | sort -r | while read -r dir; do
  base=$(basename "$dir")
  parent=$(dirname "$dir")
  # Converts lowercase, replaces low spaces/scripts with scripts and reduces multiple scripts to a single
  newbase=$(echo "$base" | tr '[:upper:]' '[:lower:]' | sed -E 's/[ _]+/-/g; s/-+/-/g')
  # Rename if the name changes
  if [ "$base" != "$newbase" ]; then
    newdir="$parent/$newbase"
    echo "renamed: $dir → $newdir"
    mv "$dir" "$newdir"
  fi
done
