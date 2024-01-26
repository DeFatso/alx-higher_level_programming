#!/usr/bin/python3
"""
    Python script that fetches url
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    print("Body response:")
    print(f"    - type: {type(response.text)}")
    print(f"    - content: {response.text}")
