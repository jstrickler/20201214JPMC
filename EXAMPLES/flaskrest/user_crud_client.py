#!/usr/bin/env python

from requests import get, put, post, patch, delete, HTTPError, codes

URL = 'http://127.0.0.1:5000/users/'

USERS = [
    ('fred', 'fred@gmail.com'),
    ('mary', 'mary@mary.com'),
    ('gecko', 'gecko@geico.com'),
]

for name, email in USERS:
    response = post(
        URL,
        data={'name': name, 'email': email},
    )
    if response.status_code != codes.OK:
        print("Error:", response.status_code)
    else:
        print(response.content.json)

