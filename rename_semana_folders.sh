#!/bin/bash

# Change to the Board of Directors
cd "d:/Jesús/Documentos/hello-python/" || exit 1

# Look for all folders that coincide with semana-<digit>
find . -type d -regextype posix-egrep -regex '.*/semana-[1-9]$' | while read -r dir; do
  parent=$(dirname "$dir")
  base=$(basename "$dir")
  # Extract the number
  num=$(echo "$base" | grep -oE '[1-9]$')
  # Build the new name
  newbase="semana-0$num"
  newdir="$parent/$newbase"
  echo "renamed: $dir → $newdir"
  mv "$dir" "$newdir"
done
