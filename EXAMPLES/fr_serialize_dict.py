import json
from flask import Flask
from flask_restful import fields, Resource, marshal_with, Api, reqparse

app = Flask(__name__)
api = Api(app)

president_fields = {  # <.>
    'termnum': fields.Integer,
    'firstname': fields.String,
    'lastname': fields.String,
    'birth_state': fields.String(attribute="birthstate"),
    'party': fields.String,
    'url': fields.Url('presidents'),  # <.>
}

with open('../DATA/presidents.json') as pres_in:  # <.>
    PRESIDENTS = json.load(pres_in)

president_count = len(PRESIDENTS['presidents'])  # <.>

error_data = {'error': 'invalid term number'}  # <.>

def invalid_term_number(term_number):  # <.>
    return not (1 <= term_number <= (president_count + 1))

class InvalidAPIRequest(Exception):  # <.>

    def __init__(self, message, status_code=400, data=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self._data = data

    def to_dict(self):
        return_value = dict(self.data or ())
        return_value['message'] = self.message
        return  return_value

class Presidents(Resource):  # <.>
    """
    Handle GET, PUT, PATCH, and DELETE posts.

    GET is only handled if a record number is specified.
    """

    @marshal_with(president_fields, envelope='president')  # <.>
    def get(self, termnum):  # <.>
        """Retrieve one record"""
        if invalid_term_number(termnum):  # <.>
            raise ValueError(f"Invalid term number: {termnum}")

        p = PRESIDENTS['presidents'][termnum - 1]
        return p  # <.>

    def put(self, termnum):  # <.>
        """Replace one record"""
        if invalid_term_number(termnum):
            raise ValueError("Invalid term number")
        return {}

    def delete(self, termnum):
        """Delete one record"""
        if invalid_term_number(termnum):
            raise ValueError("Invalid term number")
        return {}

class PresidentsList(Resource):  # <.>
    """
    Handle GET and POST requests.

    GET is only handled if no ID is specified.
    """

    @marshal_with(president_fields, envelope='presidents')  # <.>
    def get(self):
        """List all records"""
        presidents = PRESIDENTS['presidents']
        return presidents

    @marshal_with(president_fields, envelope='president')  # <.>
    def post(self):
        """Add a new record"""
        parser = reqparse.RequestParser()  # <.>
        parser.add_argument('termnum', type=int)
        parser.add_argument('firstname', type=str)
        parser.add_argument('lastname', type=str)
        parser.add_argument('birthstate', type=str)
        parser.add_argument('party', type=str)
        args = parser.parse_args()

        new_president = dict(  # <.>
            termnum=args['termnum'],
            firstname=args['firstname'],
            lastname=args['lastname'],
            birthstate=args['birthstate'],
            party=args['party'],
        )

        PRESIDENTS['presidents'].append(new_president)  # <.>

        return new_president, 201  # <.>

api.add_resource(PresidentsList, '/api/presidents')
api.add_resource(Presidents, '/api/presidents/<int:termnum>')



if __name__ == '__main__':
    app.run(debug=True)

