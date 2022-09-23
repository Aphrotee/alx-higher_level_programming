#!/bin/bash
# A Bash script that displays the size of the body of the response  to a request
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
