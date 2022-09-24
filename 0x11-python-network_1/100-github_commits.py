#!/usr/bin/python3

"""
Lists 10 commits from th erepo 'rails'
"""

import sys
import requests
if __name__ == '__main__':
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(sys.argv[1], sys.argv[2]), data={'page': 10})
    js = r.json()
    for i in range(10):
        print("{}: {}".format(js[i].get('sha'), js[i].get('commit').get('author').get('name')))