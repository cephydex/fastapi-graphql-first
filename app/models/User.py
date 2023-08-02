""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many
# from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float


class User(Model):
    """User Model"""
    __table__ = "users"
    __fillable__ = ["name", 'email', "address", "phone_number", "sex"]

    # name=str
    # address=str
    # phone_number=str
    # sex

    @has_many("id", "user_id")
    def posts(self):
        from .Post import Post

        return Post

    @has_many("id", "user_id")
    def comments(self):
        from .Comment import Comment

        return Comment


