#!/bin/bash
#Use curl to send a DELETE request to the URL and display the body
[ "$#" -eq 0 ] && echo "Usage: $0 <URL>" && exit 1; url=$1; curl -s -X DELETE "$url"

