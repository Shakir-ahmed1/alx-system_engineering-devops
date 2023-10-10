#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed in a given subreddit
"""
import requests


def top_ten(subreddit):
    """ returns top 10 posts """
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json',
                            headers=headers)
    if response.status_code != 200:
        print('None')
    else:
        r = response.json()
        count = 0
        for hots in r['data']['children']:
            if count >= 10:
                break
            if hots:
                print(hots['data']['title'])
            count += 1
