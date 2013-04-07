__author__ = 'prancer'

# API related to the application

import webapp2
import projutils
import json

from base64 import b64decode


def authenticate(auth_header):
    """
    :param r_user_id:
    :return:
    """
    [user_id, auth_id] = b64decode(auth_header.split()[1]).split(':')
    return projutils.get_user_by_id(int(user_id)).auth_id == auth_id, int(user_id)


class UserHandler(webapp2.RequestHandler):

    def get(self):
        if "Authorization" in self.request.headers.keys():
            auth_header = self.request.headers["Authorization"]
            is_allowed, user_id = authenticate(auth_header)
            if is_allowed:
                user = projutils.get_user_by_id(user_id)
                self.response.out.write(json.dumps(user.__dict__["_entity"]))
            else:
                self.response.out.write("Not Authorized")
                self.error(401)
        else:
            self.response.out.write("Forbidden")
            self.error(403)

    def post(self):
        if "Authorization" in self.request.headers.keys():
            auth_header = self.request.headers["Authorization"]
            if authenticate(auth_header):
                self.response.out.write("No operations available")
            else:
                self.response.out.write("Not Authorized")
                self.error(401)
        else:
            self.response.out.write("Forbidden")
            self.error(403)


class TagHandler(webapp2.RequestHandler):

    def get(self):
        auth_header = self.request.headers["Authorization"]
        if authenticate(auth_header):
            self.response.out.write("Yay!")
        else:
            self.response.out.write("Not Authorized")
            self.error(401)

    def post(self):
        self.response.out.write("No operations allowed!")
        self.error(501)


class PostHandler(webapp2.RequestHandler):
    def get_ids(self, post):
        return int(post.key().id())

    def get(self):
        posts_count = self.request.get("count")
        if not posts_count:
            self.error(400)
        else:
            posts_count = int(posts_count)
            posts = projutils.db.Query(projutils.Post).order('-created').fetch(posts_count)
            data_to_send = map(self.get_ids, posts)
            self.response.out.write(data_to_send)

    def post(self):
        if "Authorization" in self.request.headers.keys():
            auth_header = self.request.headers["Authorization"]
            is_allowed, user_id = authenticate(auth_header)
            if is_allowed:
                in_data = json.loads(self.request.body)

            else:
                self.response.out.write("Not Authorized")
                self.error(401)
        else:
            self.response.out.write("Forbidden")
            self.error(403)


app = webapp2.WSGIApplication([
                                  ("/api/users", UserHandler),
                                  ("/api/tags", TagHandler),
                                  ("/api/posts", PostHandler)
                              ], debug=True)