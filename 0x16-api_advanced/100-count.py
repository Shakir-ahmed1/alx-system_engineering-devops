#!/usr/bin/python3
"""
a module that counts all occurance of word in the titles of subreddits
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """ a function that queries the Reddit and count words in word_list """
    if count_dict is None:
        count_dict = {}
        for word in word_list:
            count_dict[word.lower()] = 0
    if after is None and count_dict == {}:
        return None

    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    if after is not None:
        params['after'] = after

    link = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(link, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get('data')

    articles = data.get('children')

    for article in articles:
        title = article.get('data').get('title').lower()
        for word in word_list:
            word = word.lower()
            if word in title.split():
                count_dict[word] += title.split().count(word)

    after = data.get('after')
    if after is not None:
        count_words(subreddit, word_list, after, count_dict)
    else:
        sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for key, value in sorted_count:
            if value > 0:
                print('{}: {}'.format(key, value))
