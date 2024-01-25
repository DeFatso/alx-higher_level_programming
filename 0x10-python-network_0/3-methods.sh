#!/bin/bash
#Use curl to send an OPTIONS request to the URL and display the allowed methods
[ "$#" -eq 0 ] && echo "Usage: $0 <URL>" && exit 1; url=$1; curl -sI -X OPTIONS "$url" | grep "Allow:" | cut -d " " -f 2-
