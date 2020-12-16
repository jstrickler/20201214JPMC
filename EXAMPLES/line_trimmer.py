#!/usr/bin/env python

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:  # calls .readline() behind the scenes
            yield line.rstrip('\n\r')  # <1>


# while next(); next(); next(); ...
for trimmed_line in trimmed('../DATA/mary.txt'):  # <2>
    print(trimmed_line)
