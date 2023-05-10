#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """ Program that queries Reddit API and prints the titles of
    first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
        v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    r = requests.get(url, headers=headers, params=params,
                     allow_redirects=False)

    if (r.status_code is 302):
        print("None")
        return
    if (r.status_code is 404):
        print("None")
        return
    else:
        r = r.json()
        for post in r['data']['children']:
            print(post['data']['title'])
