#!/usr/bin/python3

"""
Lists 10 commits from th erepo 'rails'
"""

import sys
import requests
if __name__ == '__main__':
    url = 'https://api.github.com/repos/'
    r = requests.get(url + '{}/{}/commits'.format(
                                    sys.argv[1],
                                    sys.argv[2]), data={'per_page': 10})
    js = r.json()
    for i in range(10):
        print("{}: {}".format(js[i].get('sha'),
                              js[i].get('commit').get('author').get('name')))
