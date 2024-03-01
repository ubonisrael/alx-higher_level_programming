#!/usr/bin/python3
"""script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter."""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    values = {'q': argv[1] if len(argv) > 1 else ""}
    res = requests.post(url, data=values)
    try:
        res = res.json()
        if len(res) == 0:
            print("No result")
        else:
            print("[{}] {}".format(res['id'], res['name']))
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")