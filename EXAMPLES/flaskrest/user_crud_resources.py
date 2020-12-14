#!/usr/bin/env python
from flask_restful import Resource
from user_crud_models import User
from user_crud_schemas import user_schema, users_schema

class UserCollection(Resource):

    def post(self):
        username, email = get_args()

        new_user = User(username, email)

        db.session.add(new_user)
        db.session.commit()

        response = user_schema.jsonify(new_user)
        response.status_code = 201
        return response

    def get(self):
        all_users = User.query.all()
        result = users_schema.jsonify(all_users)
        return result # jsonify(result.data)


class UserItem(Resource):

    def get(self, id):
        user = User.query.get(id)
        return user_schema.jsonify(user)

    def put(self, id):
        username, email = get_args()

        user = User.query.get(id)

        user.email = email
        user.username = username

        db.session.commit()
        return user_schema.jsonify(user)

    def patch(self, id):
        username, email = get_args()

        user = User.query.get(id)

        print("USERNAME:", username)
        print("EMAIL:", email)
        if username is not None:
            user.username = username
        if email is not None:
            user.email = email

        db.session.commit()
        return user_schema.jsonify(user)


    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return user_schema.jsonify(user)

def get_args():
    args = parser.parse_args()

    username = args['username']
    email = args['email']
    return username, email


