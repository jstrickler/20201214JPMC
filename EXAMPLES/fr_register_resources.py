import json
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


STUDENTS = [
    'Melinda Gates',
    'Steve Jobs',
    'Larry Wall',
    'Paul Allen',
    'Larry Ellison',
    'Bill Gates',
    'Mark Zuckerberg',
    'Sergey Brin',
    'Larry Page',
    'Linus Torvalds',
]


class Teacher(Resource):
    def get(self):
        return {'name': 'Dennis Ritchie'}

class Students(Resource):
    def get(self, id):
        return {'name': STUDENTS[id]}

class StudentsList(Resource):
    def get(self):
        return {'students': {i: s for i, s in enumerate(STUDENTS)}}

api.add_resource(Teacher, '/api/teacher')
api.add_resource(Students,'/api/students/<int:id>')
api.add_resource(StudentsList,'/api/students')


if __name__ == '__main__':
    app.run(debug=True)

