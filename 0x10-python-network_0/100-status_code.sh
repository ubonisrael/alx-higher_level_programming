#!/bin/bash
# sends a get request and prints the status code
curl -s -o /dev/null "$1" -w '%{http_code}'
