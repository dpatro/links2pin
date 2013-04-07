#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import jinja2
import os

import projutils

from google.appengine.api import users


class MainHandler(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        content = ""
        if cur_user is None:
            self.redirect(users.create_login_url())
        else:
            if not projutils.check_if_user(cur_user.email()):
                user_id, auth_id = projutils.add_user(cur_user)
                status = "New User with id: %d and %s" % (user_id, auth_id)
            else:
                user_id = projutils.get_user_id_by_email(cur_user.email())
                status = "Old User with id: %d"%user_id

            # Get 5 posts
            posts = projutils.db.Query(projutils.Post).order('-created').fetch(5)

            template_values = {
                "title": "Link It",
                "posts": posts,
                "status": status,
                "user_id": user_id,
                "logout_url": users.create_logout_url("/")
            }

            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(template_values))

    def post(self):
        #self.response.out.write("yay!")
        link = str(self.request.get("link"))
        user_id = int(self.request.get("user"))
        tag_id = int(self.request.get("tag"))

        projutils.create_post(link, user_id, tag_id)
        self.redirect("/")

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),"templates/")))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
