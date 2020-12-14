#!/usr/bin/env python
# (c) 2016 John Strickler
#
import random
from flask import Flask
from flask_restful import Resource, Api
import logging
from cheeses import CHEESES, cheese_makers

app = Flask(__name__)
api = Api(app)

# configure logging
handler = logging.FileHandler("cheeseapi.log")
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

class Cheese(Resource):
    def get(self):
        cheese_maker = random.choice(cheese_makers)
        cheese = CHEESES.get(cheese_maker)
        app.logger.info('Selected {} {}'.format(cheese_maker, cheese))
        return {cheese_maker: cheese}

api.add_resource(Cheese, '/api/1.0/Cheese')

if __name__ == '__main__':
    app.run(debug=True)
