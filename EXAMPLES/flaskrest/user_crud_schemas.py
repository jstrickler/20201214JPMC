#!/usr/bin/env python

def get_user_schema_class(marshmallow):
    class UserSchema(marshmallow):
        class Meta:
            # Fields to expose
            fields = ('username', 'email')
    return UserSchema


