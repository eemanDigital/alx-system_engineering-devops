import requests


def count_words(subreddit, word_list, after=None, matches={}):
    """
    Queries the Reddit API recursively, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should
    count as javascript, but java should not).
    """
    if not word_list:
        return None

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get('data')
    after = data.get('after')
    children = data.get('children')

    for child in children:
        title = child.get('data').get('title').lower().split()
        for word in word_list:
            count = title.count(word.lower())
            if count > 0:
                matches[word] = matches.get(word, 0) + count

    if after is None:
        if not matches:
            return None

        sorted_matches = sorted(matches.items(), key=lambda x: (-x[1], x[0]))
        for match, count in sorted_matches:
            print("{}: {}".format(match, count))

    else:
        count_words(subreddit, word_list, after, matches)
