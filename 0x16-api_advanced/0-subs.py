#!/usr/bin/python3
"""
contain the function that returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns
    the number of subscribers """
    if not subreddit or type(subreddit) is not str:
        return 0
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win; x64)'}
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    return 0
