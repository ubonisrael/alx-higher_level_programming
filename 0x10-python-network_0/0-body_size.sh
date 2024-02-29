#!/bin/bash
# A script that gets the content lenght of an url
curl -sI "$1" | grep -i 'Content-Length' | cut -d ' ' -f 2
