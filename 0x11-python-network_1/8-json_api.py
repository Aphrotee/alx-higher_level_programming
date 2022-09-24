#!/usr/bin/python3

"""
This is a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
import sys

if __name__ == '__main__':
    r = requests.get('http://0.0.0.0:5000/search_user', data={'q': sys.argv[1]})
    if r.headers.get('content-type') == 'application/json':
        try:
            js = r.json()
            if len(js) == 0:
                print("No result")
            else:
                print("{}: {}".format(js.get('id'), js.get('name')))
        except requests.JSONDecodeError:
            print("Not a valid JSON")
