#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys


def sender():
    address = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(address)
    data = data.encode("ascii")
    req =urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlepon(req) as response:
        html = response.read()
        print(html.decode("utf-8"))

if __name__ == "__main__":
    sender()
