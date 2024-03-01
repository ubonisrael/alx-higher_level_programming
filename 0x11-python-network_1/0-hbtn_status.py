#!/usr/bin/python3
"""Fetches an url using urllib"""
import urllib

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as res:
        msg = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(msg)))
        print("\t- content: {}".format(msg))
        print("\t- utf-8 content: {}".format(msg.decode("utf-8")))
