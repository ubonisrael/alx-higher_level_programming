#!/usr/bin/python3
"""a  script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)"""
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except error.URLError as e:
        print(e.code)
