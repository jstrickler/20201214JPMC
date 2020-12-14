#!/usr/bin/env python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from flask_marshmallow import Marshmallow
from user_crud_models import User
from user_crud_schemas import get_user_schema
from user_crud_resources import UserItem, UserCollection

def main():
    basename = os.path.abspath(os.path.basename(__file__))
    db_name = os.path.splitext(basename)[0] + '.db'

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_name)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    api = Api(app)

    parser = reqparse.RequestParser()
    parser.add_argument('username')
    parser.add_argument('email')

    UserSchema = get_user_schema_class()
    user_schema = UserSchema()
    users_schema = UserSchema(many=True)

    api.add_resource(UserCollection, '/users')
    api.add_resource(UserItem, '/users/<int:id>')

    app.run(debug=True)


if __name__ == '__main__':
    if not os.path.exists(db_name):
        db.create_all()
    main()
