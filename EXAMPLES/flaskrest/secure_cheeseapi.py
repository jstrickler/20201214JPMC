#!/usr/bin/env python
# (c) 2016 John Strickler
#
import random
from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from cheeses import CHEESES, cheese_makers

auth = HTTPBasicAuth()

app = Flask(__name__)
api = Api(app)

USERS = {
    'mary': '$3cr3t',
    'bob': 'l0lz',
}

@auth.verify_password
def verify_password(user, password):
    if USERS.get(user) == password:
        return True
    else:
        return False

class Cheese(Resource):
    decorators = [auth.login_required]

    def get(self):
        cheese_maker = random.choice(cheese_makers)
        cheese = CHEESES.get(cheese_maker)
        return {cheese_maker: cheese}

api.add_resource(Cheese, '/api/1.0/Cheese')

if __name__ == '__main__':
    app.run(debug=True)
