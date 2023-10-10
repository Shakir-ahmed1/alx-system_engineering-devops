#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed in a given subreddit
"""
import requests


def top_ten(subreddit):
    """ returns top 10 posts """
    headers = {'User-Agent': 'Mozilla/5.0'}
    link = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(link, headers=headers)
    r = response.json()
    if response.status_code != 200 or not r.get('data').get('children'):
        print('None')
    else:
        count = 0
        for hots in r.get('data').get('children'):
            if count >= 10:
                break
            if hots:
                try:
                    print(hots.get('data').get('title'))
                except Exception:
                    print()
            count += 1
