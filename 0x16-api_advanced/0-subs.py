#!/usr/bin/python3
""" a module that gets number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ returns number of subscribers of a subreddit """
    headers = {'User-Agent': 'Mozilla/5.0'}
    link = 'https://www.reddit.com/r/{}/about.json'.format(subreddit) 
    response = requests.get(link, headers=headers)
    r = response.json()
    if not r or 'error' in r:
        return 0
    return r['data']['subscribers']
