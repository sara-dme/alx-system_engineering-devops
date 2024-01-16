#!/usr/bin/python3
""" Module that contains recursive function
that queries the Reddit API and returns a list
containing the titles of all hot articles for
a given subreddit.
"""
import requests

def recurse(subreddit, after=None):
    """ the function that queries tha Reddit API"""
    headers = {"User_Agent": ""}
    params = {"after": after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url, allow_redirects=False,
                       headers=headers, params=params)
    posts = []
    if req.status_code == 200:
        data = req.json()
        after = data["data"]["after"]
        if after is None:
            return posts
        for p in data["data"]["children"]:
            posts.append(p["data"]["title"])
        next = recurse(subreddit, after)
        posts.extend(next)
        return posts
    return None
