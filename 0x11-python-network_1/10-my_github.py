#!/usr/bin/python3
"""script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id"""
from sys import argv
from requests.auth import HTTPBasicAuth
import requests

if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    try:
        print(res.json()['id'])
    except KeyError as e:
        print("None")
