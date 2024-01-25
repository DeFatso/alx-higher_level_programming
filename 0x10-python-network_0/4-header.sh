#!/bin/bash
# Use curl to send a GET request with a custom header and display the body
[ "$#" -eq 0 ] && echo "Usage: $0 <URL>" && exit 1; url=$1; curl -s -H "X-School-User-Id: 98" "$url"
