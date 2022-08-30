from flask_mongoengine import MongoEngine
from mongoengine import *
from mongoengine.connection import connect
from mongoengine.fields import *
from mongoengine.document import *

connect("Login")

class User(DynamicDocument):
    name = StringField()
    email = EmailField()
    num = StringField()
    Age = IntField
    Rating = StringField()
    Grade = StringField()
