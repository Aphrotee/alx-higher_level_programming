#!/usr/bin/python3

"""
This is a Python script that fetches https://alx-intranet.hbtn.io/status
"""


import urllib
import urllib.request
if __name__ == '__main__':
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()
    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html.decode('utf-8')))