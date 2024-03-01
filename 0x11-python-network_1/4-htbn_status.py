#!/usr/bin/python3
"""Fetches an url using urllib"""
import requests

if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print(res)
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
    # print("\t- utf8 content: {}".format(msg.decode("utf-8")))
