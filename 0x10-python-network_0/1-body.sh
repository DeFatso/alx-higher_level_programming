#!/bin/bash
# Script that takes in a URL, sends a request to that URL
curl -s -w "%{http_code}" $1
