#!/bin/bash

commands=("python3" "flutter" "docker" "psql" "xcode-select")

for cmd in "${commands[@]}"; do
    if command -v "$cmd" >/dev/null 2>&1; then
        continue
    else
        echo "$cmd is not installed. Please install all pre-requisites before running this script."
        exit 1
    fi
done

echo "All required commands have been installed. Moving on..."

