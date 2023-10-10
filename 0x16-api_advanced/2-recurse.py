#!/usr/bin/python3
"""
module that returns a list containing the titles of all hot articles for a
given subreddit
"""
import requests


def recurse(subreddit, params={}, hot_list=[]):
    """ returns a list of titles """
    if params is not None:
        link = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(link, headers=headers, params=params)
        r = response.json()
        if not r or 'error' in r:
            return None

        for post in r['data']['children']:
            hot_list.append(post['data']['title'])

        params = {'after': r['data']['after']}
        if params['after']:
            return recurse(subreddit, params=params, hot_list=hot_list)
    return hot_list
