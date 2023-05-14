#!/usr/bin/python3

""" BaseModel module that is imported from models directory"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ A class Amenity that inherits from BaseModel

    Attributes:
        name (str): Name of the amenity provided
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes an instance"""
        super().__init__(*args, **kwargs)
