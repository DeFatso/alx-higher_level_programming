#!/usr/bin/python3
"""
    Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

import requests
import sys
if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    headers = {
        'Authorization': f'Basic {username}:{token}',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        user_data = response.json()
        user_id = user_data.get('id')

        print(f"Your GitHub ID: {user_id}")

    except requests.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
