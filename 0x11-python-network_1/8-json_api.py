#!/usr/bin/python3
"""
    Python script that takes in a letter and sends a POST
    equest to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    q = sys.argv[1]
    q = letter if letter else ""

    data = {'q': q}

    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data=data)
        response.raise_for_status()

        json_data = response.json()

        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
