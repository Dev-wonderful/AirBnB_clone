#!/usr/bin/python3
""" BaseModel module that is imported from models directory """

from models.base_model import BaseModel

""" A class City that inherits from BaseModel class """

class City(BaseModel):
    """ Public class attributes """

    state_id = ""
    name = ""
