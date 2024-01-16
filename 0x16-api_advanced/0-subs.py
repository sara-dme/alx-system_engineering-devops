#!/usr/bin/python3
"""
contain the function that returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns
    the number of subscribers """
    url = "https://www.reddit.com/r/{0}/about.json".format(str(subreddit))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/120.0.0.0 Safari/537.36'}
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    return 0
