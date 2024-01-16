#!/usr/bin/python3
"""
contain thei function that prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit)
    """ function that prints the 10 first post listed
    for a given subscribers """
    if not subreddit or type(subreddit) is not str:
        return 0
    url = 'http://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': ''}
    req = requests.get(url, allow_redirects=False, headers=headers)
    if req.status_code == 200:
        data = req.json().get('data')
        article = data.get("children")
        for a in article:
            data = a.get("data")
            print(data.get("title"))
        else:
            print(None)
