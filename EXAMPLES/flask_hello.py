#!/usr/bin/env python
from flask import Flask
# add extensions here...

app = Flask(__name__)  # <1>  add config info here

#  www.cia.gov/country/Spain

@app.route('/country/<string:country>')  # <2>
def visit(country):  # <3>
    return f'<h1>Visit beautiful {country}!</h1>' # <4>

@app.route('/')
def index():
    return '<h1>Hello from this silly app!</h1>'

@app.route('/animal/<string:animal>')
def zoo(animal):
    return(f"<h1>{animal}s are wonderful</h1>")


# app.register_route(index, '/')

if __name__ == '__main__':
    app.run(debug=True) # <5>
