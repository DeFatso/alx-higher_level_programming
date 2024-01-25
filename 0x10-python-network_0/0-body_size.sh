#!/usr/bin/env bash
#script that takes in a URL, sends a request to that URL, and
#displays the size of the body of the response

url=$1

response=$(curl -sI $url)
content_length=$(echo "$response" | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n')
echo ${content_length}
