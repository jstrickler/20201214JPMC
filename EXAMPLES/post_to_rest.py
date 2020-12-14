#!/usr/bin/env python
from datetime import datetime
import time
import requests

URL = 'http://httpbin.org/post'

for i in range(3):
    response = requests.post(  # <1>
        URL,
        data={'date': datetime.now(),
            'label': 'test_' + str(i)
        },
        cookies={'python': 'testing'},
        headers={'X-Python': 'Guido van Rossum'},
    )
    if response.status_code in (requests.codes.OK, requests.codes.created):
        print(response.content.decode())
        time.sleep(2)

    print(response.status_code)
    print(response.content.decode())
