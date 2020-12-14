import json
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)  # <1>
api = Api(app)  # <2>


class Student(Resource):  # <3>
    def get(self):  # <4>
        return {'name': 'Jane Student'}  # <5>

api.add_resource(Student,'/api/student', '/api/auditor')  # <6>
# api.add_resource(Student,'/api/student')  # <6>


if __name__ == '__main__':
    app.run(debug=True)  # <7>

