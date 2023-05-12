#!/usr/bin/python3
""" queries an api and returns required info."""
import requests


def recurse(subreddit, hotlist=[], count=0):
    """
    recursive function that queries the Reddit API
    and returns a list containing the titles of all
    hot articles for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "my_reddit_api_v1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        children = response.json().get("data").get("children")
        title = children[count].get("data").get("title")
        hotlist.append(title)
        count += 1
        if count < len(children):
            recurse(subreddit, hotlist, count)
        if len(hotlist) == 0:
            return None
        return hotlist
    else:
        return None
