#!/usr/bin/env python
# (c) 2016 John Strickler
#
import random
from flask import Flask
from flask_restful import Resource, Api
from cheeses import CHEESES, cheese_makers

app = Flask(__name__)
api = Api(app)


class Cheese(Resource):
    """
    The Cheese resource
    """
    def get(self):
        """
        Retrieve a random cheesery and cheese.

        :return:  Dict of cheesery and cheese as JSON object
        """
        cheese_maker = random.choice(cheese_makers)
        cheese = CHEESES.get(cheese_maker)
        return {cheese_maker: cheese}

api.add_resource(Cheese, '/cheese')

if __name__ == '__main__':
    app.run(debug=True)
