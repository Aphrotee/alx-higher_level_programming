#!/bin/bash
# A Bash script that displays the size of the body of the response  to a request
curl -Is "$1" | grep "Content-Length" | tr " " "\n" | tail -1
