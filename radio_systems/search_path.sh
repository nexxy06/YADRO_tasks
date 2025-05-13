#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file_to_search> <parameter>"
    exit 1
fi

real_path="$(realpath "$1")"

grep "$2" $real_path
