#!/usr/bin/python3
""" fetches an url"""

import urllib.requests

url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    with urllib.requests.urlopen(url) as resonse
    content = response.read()
    utf8_content = content.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {utf8_content}")
