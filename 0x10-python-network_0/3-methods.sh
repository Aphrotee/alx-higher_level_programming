#!/bin/bash
# This is a Bash script that takes in a URL and displays all HTTP methods.
curl -X OPTIONS -sI "$1" | grep "Allow" | tr ':' '\n' | tail -1
