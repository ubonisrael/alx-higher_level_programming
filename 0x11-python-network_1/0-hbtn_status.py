#!/usr/bin/python3
# Fetches an url using urllib
from urllib import request

if __name__ == "__main__":
    req = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(req) as res:
        msg = res.read()
        print("Body response:")
        print("    - type: {}".format(type(msg)))
        print("    - content: {}".format(msg))
        print("    - utf-8 content: {}".format(msg.decode("utf-8")))
