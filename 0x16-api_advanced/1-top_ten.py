#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed in a given subreddit
"""
import requests


def top_ten(subreddit):
    """ returns top 10 posts """
    response = requests.get('https://www.reddit.com/r/programming/hot.json')
    r = response.json()
    if not r or 'error' in r:
        print('None')
    else:
        count = 0
        for hots in r['data']['children']:
            if count >= 10:
                break
            if hots:
                print(hots['data']['title'])
            count += 1
