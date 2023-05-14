#!/usr/bin/python3

""" The BaseModel module and File storage module"""
from models.base_model import BaseModel


class User(BaseModel):
    """" A class User that inherits from the BaseModel class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializing an instance and calling the super class"""
        super().__init__(*args, **kwargs)
