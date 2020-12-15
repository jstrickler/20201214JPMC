#!/usr/bin/env python
import csv
import pandas as pd

with open('../DATA/knights.csv') as knights_in:
    rdr = csv.reader(knights_in)  # <1>
    for name, title, color, quest, comment, number, ladies in rdr:  # <2>
        print('{:4s} {:9s} {}'.format(
            title, name, quest
        ))

# 'names' means "column names"
df = pd.read_csv('../DATA/knights.csv', names='name title color quest comment num ladies'.split())
print(df)
print(df.loc[:,'num'])
print(df.loc[:,'num'].sum())
