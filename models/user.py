#!/usr/bin/python3
""" The BaseModel module and File storage module"""
from models.base_model import BaseModel
from models import storage

"""" A class User that inherits from the BaseModel class"""
class User(BaseModel):
""" Public class attributes"""

    email = " "
    password = " "
    first_name = " "
    last_name = " "
        
