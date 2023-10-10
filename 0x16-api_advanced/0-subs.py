#!/usr/bin/python3
""" a module that gets number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ returns number of subscribers of a subreddit """
    response = requests.get('https://www.reddit.com/r/programming/about.json')
    r = response.json()
    if not r or 'error' in r:
        return 0
    return r['data']['subscribers']
