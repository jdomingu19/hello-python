#!/bin/bash

# Change to the Board of Directors
cd "d:/Jesús/Documentos/hello-python/" || exit 1

# Find all files (recursive), order the highest route depth from greater
find . -type f | sort -r | while read -r filepath; do
  dir=$(dirname "$filepath")
  filename=$(basename "$filepath")
  # Converts lowercase, replaces spaces by _ and eliminates scripts, then reduces multiple _ to one
  newfilename=$(echo "$filename" | tr '[:upper:]' '[:lower:]' | sed -E 's/[ ]+/_/g; s/-//g; s/_+/_/g')
  newfilepath="$dir/$newfilename"
  # Rename if the name changes
  if [ "$filepath" != "$newfilepath" ]; then
    echo "renamed: $filepath → $newfilepath"
    mv "$filepath" "$newfilepath"
  fi
done
