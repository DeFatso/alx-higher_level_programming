#!/bin/bash
# This script sends a POST request with specific parameters to a given URL and displays the response body
curl -sX POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD" | grep -oP '(?<=<body>).*(?=<\/body>)'
