#!/usr/bin/python3
""" BaseModel module that is imported from models directory"""
from models.base_model import BaseModel

""" A class Review that inherits from BaseModel"""
class Review(BaseModel):
    """ Public class attributes"""

    place_id = " "
    user_id = " "
    text = " "
