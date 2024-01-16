#!/usr/bin/python3
"""
contain thei function that prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """ function that prints the 10 first post listed
    for a given subscribers """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; '
               'rv:121.0) Gecko/20100101 Firefox/121.8'}
    params = { "limit": 10 }
    req = requests.get(url, allow_redirects=False, params=params,
                       headers=headers)
    if req.status_code == 200:
        data = req.json().get('data')
        article = data.get("children")
        for a in article:
            data = a.get("data")
            print(data.get("title"))
    else:
            print(None)
