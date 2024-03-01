#!/usr/bin/python3
"""a  script that takes in a URL and an email,
sends request to the passed URL
and displays the body of the response"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        res = requests.get(url)
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
