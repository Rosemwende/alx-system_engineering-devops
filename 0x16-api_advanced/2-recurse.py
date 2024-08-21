#!/usr/bin/python3
"""Python script to recursively query the Reddit API and
return a list of all hot article titles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch all hot article titles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list to accumulate hot
	article titles (default is an empty list).
        after (str): The after parameter for pagination (default is None).
    
    Returns:
        list: A list of hot article titles or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                return hot_list if hot_list else None

            for post in posts:
                hot_list.append(post.get('data', {}).get('title'))
                
            after = data.get('data', {}).get('after', None)
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
