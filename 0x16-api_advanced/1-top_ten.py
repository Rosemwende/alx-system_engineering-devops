#!/usr/bin/python3
"""Python script to query the Reddit API and print the
titles of the top 10 hot posts from a given subreddit.
"""

import requests

def top_ten(subreddit):
    """Print the titles of the top 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for i, post in enumerate(posts[:10]):
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except Exception as e:
        print(f"An error occurred: {e}")
        print(None)
