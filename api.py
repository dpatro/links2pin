__author__ = 'prancer'

# API related to the application

import webapp2
import projutils
import logging

from base64 import b64decode


def authenticate(auth_header):
    """
    :param r_user_id:
    :return:
    """
    [user_id, auth_id] = b64decode(auth_header.split()[1]).split(':')
    return projutils.get_user_by_id(int(user_id)).auth_id == auth_id


class UserHandler(webapp2.RequestHandler):

    def get(self):
        auth_header = self.request.headers["Authorization"]
        if authenticate(auth_header):
            self.response.out.write("Yay!")
        else:
            self.response.out.write("Not Authorized")
            self.error(401)

    def post(self):
        auth_header = self.request.headers["Authorization"]
        if authenticate(auth_header):
            self.response.out.write("Yay!")
        else:
            self.error(401)


class TagHandler(webapp2.RequestHandler):

    def get(self):
        auth_header = self.request.headers["Authorization"]
        if authenticate(auth_header):
            self.response.out.write("Yay!")
        else:
            self.response.out.write("Not Authorized")
            self.error(401)

    def post(self):
        auth_header = self.request.headers["Authorization"]
        if authenticate(auth_header):
            self.response.out.write("Yay!")
        else:
            self.error(401)


class PostHandler(webapp2.RequestHandler):

    def get(self):
        auth_header = self.request.headers["Authorization"]
        if authenticate(auth_header):
            self.response.out.write("Yay!")
        else:
            self.response.out.write("Not Authorized")
            self.error(401)

    def post(self):
        auth_header = self.request.headers["Authorization"]
        if authenticate(auth_header):
            self.response.out.write("Yay!")
        else:
            self.error(401)


app = webapp2.WSGIApplication([
                                  ("/api/users", UserHandler),
                                  ("/api/tags", TagHandler),
                                  ("/api/posts", PostHandler)
                              ], debug=True)