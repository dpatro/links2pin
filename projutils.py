__author__ = 'prancer'

import logging

from projdb import *
from urllib import urlopen
from bs4 import BeautifulSoup
from uuid import uuid4


def extract_data_from_link(link):
    """
    :param link:
    :return:
    """
    title = "Default Title"
    body = "Default Body"

    try:
        data = urlopen(link).read()
    except BaseException:
        logging.error("Couldn't open Url")
    else:
        # Parse the html doc
        doc = BeautifulSoup(data)
        title = str(doc.title.string)
        body = str(doc.body.p.string)
        del doc
    finally:
        return title, body + " ..."


# User related functions below
def check_if_user(email):
    """Checks if email is already registered
    Input:
        email : string
    Output:
        Boolean : true if user is already registered else false
    """
    if db.Query(User).filter("email =", email).count() == 1:
        return True
    else:
        return False


def add_user(user):
    """Adds new user to DB
    Input:
        email : String
    Output:
        Boolean : True for successful addition Else False
    """
    try:
        new_author = User()
        new_author.name = user.nickname()
        new_author.email = user.email()
        new_author.auth_id = str(uuid4())
        new_author.put()
    except BaseException:
        logging.error("Couldn't add new user")
        return -1
    else:
        return new_author.key().id(), new_author.auth_id


def get_user_by_id(user_id):
    """Get User by its id
    """
    return User.get_by_id(user_id)


def get_user_id_by_email(email):
    res = db.Query(User).filter("email =", email)
    return res[0].key().id()


# Tags related functions below
def get_tag_by_id(tag_id):
    """
    Get Tag by its id
    :param tag_id:
    """
    return Tag.get_by_id(tag_id)


def create_tag(tag_name):
    """
    Create a new tag
    :param tag_name:
    :return:
    """
    try:
        new_tag = Tag()
        new_tag.name = tag_name
        new_tag.put()
    except BaseException:
        logging.error("Couldn't create Tag")
        return -1
    else:
        return new_tag.key().id()


# Posts related functions below
def create_post(link, user_id, tag_id):
    """
    Create new post
    :param link:
    :param user_id:
    :param tag_id:
    :return:
    """
    (title, body) = extract_data_from_link(link)

    new_post = Post()
    new_post.url = link
    new_post.title = title
    new_post.body = body
    new_post.user = user_id
    new_post.tag = tag_id

    #try:
    new_post.put()
    #except BaseException:
    #    logging.error("Couldn't Create new post")
    #    return -1
    #else:
    return new_post.key().id()


def get_post_by_id(post_id):
    """
    Get post using post id
    :param post_id:
    :return post:
    """
    return Post.get_by_id(post_id)