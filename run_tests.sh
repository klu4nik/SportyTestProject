#!/bin/bash

# Script to run tests from any directory
# Usage: ./run_tests.sh [test_path]

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the script's directory
cd "$SCRIPT_DIR"

# Activate virtual environment
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

# Check for USER_ID environment variable
if [ -z "$USER_ID" ]; then
    echo "Error: USER_ID environment variable is not set."
    exit 1
fi

# Run pytest with the provided test path or default to all tests
if [ $# -eq 0 ]; then
    pytest
else
    pytest "$1"
fi