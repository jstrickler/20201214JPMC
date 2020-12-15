#!/usr/bin/env python
#
import json
from datetime import date


class Parrot():  # <1>
    def __init__(self, name, color):
        self._name = name
        self._color = color

    @property
    def name(self):  # <2>
        return self._name

    @property
    def color(self):
        return self._color

    def to_json(self):
        pass

parrots = [  # <3>
    Parrot('Polly', 'green'),  #
    Parrot('Peggy', 'blue'),
    Parrot('Roger', 'red'),
]

data = {  # <10>
    'time_stamp': [1, 2, 3],
    'ham': ('a', 'b', 'c'),
    'toast': date(2014, 8, 1),
    'parrots': parrots,
}

try:
    print(json.dumps(data, indent=4))  # <11>
except Exception as err:
    print(err)

def encode(obj):  # <4>
    if isinstance(obj, date):  # <5>
        return obj.ctime()  # <6>
    elif isinstance(obj, Parrot):  # <7>
        return {'name': obj.name, 'color': obj.color}  # <8>
    elif hasattr(obj, 'to_json'):
        return obj.to_json()
    return obj  # <9>



print(json.dumps(data, default=encode, indent=4))  # <11>
