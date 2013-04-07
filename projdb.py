__author__ = 'prancer'


from google.appengine.ext import db


class User(db.Model):
    name = db.StringProperty()
    email = db.EmailProperty()
    auth_id = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)


class Tag(db.Model):
    name = db.StringProperty()


class Post(db.Model):
    url = db.LinkProperty()
    title = db.StringProperty()
    body = db.StringProperty()
    img = db.StringProperty()
    tag = db.IntegerProperty()
    user = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add=True)


class User_to_Post(db.Model):
    user_id = db.IntegerProperty()
    post_ids = db.ListProperty(int)
    posts_count = db.IntegerProperty()


class Tag_to_Post(db.Model):
    tag_id = db.IntegerProperty()
    post_ids = db.ListProperty(int)