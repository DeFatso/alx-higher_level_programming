#!/bin/bash
# Script that takes in a URL, sends a request to that URL
[ "$#" -eq 0 ] && echo "Usage: $0 <URL>" && exit 1; url=$1; [ $(curl -s -o /dev/null -w "%{http_code}" "$url") -eq 200 ] && curl -s "$url"
