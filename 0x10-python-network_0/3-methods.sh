#!/bin/bash
# A script that gets the http methods supported by a server
curl -sI "$1" | grep -i 'Allow' | cut -d " " -f 2-
