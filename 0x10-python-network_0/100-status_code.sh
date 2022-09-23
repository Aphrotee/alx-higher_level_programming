#!/bin/bash
# This script sends a request to a URL passed as an argument, and displays only the status code.
curl -s -w "%{http_code}" "$1" -o /dev/null
