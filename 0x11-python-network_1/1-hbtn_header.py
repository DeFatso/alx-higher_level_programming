#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL and displays the value
    of the X-Request-Id variable found in the header of the response.
"""
from urllib import request
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    with request.urlopen(url) as response:
        x_req_id = response.headers.get('X-Request-Id')
        print(x_req_id)
