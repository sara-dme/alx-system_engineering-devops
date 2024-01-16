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
    headers = {'User-agent': '0x16-api_advanced:project:v1.0.0'}
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        r = r.json()
    else:
        return 0
    return r.get('data', {}).get('subscribers', 0)
