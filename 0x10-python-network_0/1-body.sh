#!/bin/bash
# Script that takes in a URL, sends a request to that URL
url=$1; response=$(curl -sI "$url"); content_length=$(echo "$response" | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n'); echo "${content_length}"
