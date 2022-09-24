#!/usr/bin/python3
"""
This is a Python script that fetches https://alx-intranet.hbtn.io/status
"""


import requests

if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.content.decode('utf-8'))))
    print("\t- content: {}".format(r.content.decode('utf-8')))
