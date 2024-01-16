#!/usr/bin/python3
"""recursive function that queries the reddit API"""
import requests


def count_words(subreddit, word_list, titles=[], after=None):
     """ function doc """
     if after is None:
         url = "https://www.reddit.com/r/{}/hot.json?after={}"\
                 .format(subreddit, after)
         headers = {'User-Agent': 'Custom Browser'}
         req = requests.get(url, headers=headers, allow_redirects=False)
         if req.status_code == 200:
             data = req.json().get('data')
             after = data.get("after")
             article = data.get("children")
             for a in article:
                 titles.append(article.get("data").get("title"))
             count_words(subreddit, word_list, titles, after)
         else:
             count = {}
             word_list = [word.lower() for word in word_list]
             words = []
             for word in word_list:
                 if word not in words:
                     words.append(word)
             for t in titles:
                 for w in words:
                     wt = [w.lower() for w in t.split(" ")]
                     for wtt in wt:
                         if w == wtt:
                             count[w] = count.get(w, 0) + 1
             count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
             if count is not {}:
                 for item in count:
                     print("{}: {}".format(item[0], item[1]))
                        
              
