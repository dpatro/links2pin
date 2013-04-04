__author__ = 'prancer'


from google.appengine.ext import db


class User(db.Model):
    name = db.StringProperty()
    email = db.StringProperty()
    auth_id = db.StringProperty()


class Tag(db.Model):
    name = db.StringProperty()


class Post(db.Model):
    url = db.StringProperty()
    title = db.StringProperty()
    body = db.StringProperty()
    img = db.StringProperty()
    tag = db.IntegerProperty()
    user = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add=True)