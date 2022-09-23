#!/usr/bin/python3
"""
This is a Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""


import urllib
import sys
from urllib.error import HTTPError
import urllib.parse
import urllib.request


if '__name__' == '__main__':
    req = urllib.request.Request(sys.argv[1], data)
    try:
        response = urllib.request.urlopen(req)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
        