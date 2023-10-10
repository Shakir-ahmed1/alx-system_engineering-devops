#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sortedcount of given keywords
"""
import requests


def sort_display(sa):
    sc = []
    for sb in sa:
        sc.append([sb, sa[sb]])
    sd = sorted(sc, key=lambda x: x[1], reverse=True)
    for se in sd:
        print("{}: {}".format(se[0], se[1]))


def count_words(subreddit, word_list, params={}, result={}):
    """ prints the occurance of the word list in titles """
    if params is not None:
        link = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(link, headers=headers, params=params)
        r = response.json()
        if not r or 'error' in r:
            return None
        if result == {}:
            for word in word_list:
                result[word] = 0

        for post in r['data']['children']:
            for wr in result:
                pst = [ps.lower() for ps in post['data']['title'].split(' ')]
                temp = pst.count(wr.lower())
                result[wr] += temp
        params = {'after': r['data']['after']}
        if params['after']:
            count_words(subreddit, word_list, params=params, result=result)

    r_set = list(set([rs.lower() for rs in result if result[rs] != 0]))
    r_dict = {}
    for rs in r_set:
        r_dict[rs] = 0
    for rs in result:
        if result[rs] != 0:
            r_dict[rs.lower()] += result[rs]
    if params['after'] is None:
        sort_display(r_dict)
