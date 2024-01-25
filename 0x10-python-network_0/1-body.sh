#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body for a 200 status code
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
