#!/usr/bin/python3
"""Module to create user"""
from models.base_model import BaseModel
from models.__init__ import storage


class User(BaseModel):
    """A class to template users

    Attributes:
        first_name (str): first name of user
        last_name (str): last name of user
        email (str): email of user
        password (str): password of user
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """Initializes an instance"""
        super().__init__(*args, **kwargs)

    # def save(self):
    #     """Adds attribute to the object dictionary"""
    #     obj = self.to_dict()
    #     storage.save(obj)
