#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API for a given subreddit and returns a list
    of all hot article titles.

    subreddit: str
        The name of the subreddit to query.

    hot_list: list, optional
        The list of hot article titles. Defaults to an empty list.

    after: str, optional
        The ID of the last item in the previous page of results.
        Defaults to None.

    Returns
    -------
    list of str
        A list of hot article titles for the given subreddit. Returns None if
        the subreddit is invalid or if no results are found.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        hot_list += [post['data']['title'] for post in data['children']]
        after = data['after']
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
