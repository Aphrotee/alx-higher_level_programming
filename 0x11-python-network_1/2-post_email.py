#!/usr/bin/python3
"""
This is a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


import urllib
import sys
import urllib.parse
import urllib.request


if __name__ == '__main__':
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode('utf-8'))
