#!/bin/bash
# sends a json file to URL
curl -X "POST" -H "Content-Type: application/json" -d @"$2" "$1"
