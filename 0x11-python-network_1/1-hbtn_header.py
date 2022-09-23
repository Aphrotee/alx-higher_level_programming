#!/usr/bin/python3
"""
This is a Python script that takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""


import urllib
import sys
import urllib.request


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        head_dict = dict(response.headers)
        print(head_dict.get('X-Request-Id'))
