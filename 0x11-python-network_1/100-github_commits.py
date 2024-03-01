#!/usr/bin/python3
"""script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10".\
        format(argv[2], argv[1])
    res = requests.get(url)
    try:
        res = res.json()
        for i in res:
            print("{}: {}".format(i['sha'],
                                  i['commit']['author']['name']))
    except KeyError as e:
        print("None")
