#!/usr/bin/python3
""" BaseModel module that is imported from models directory"""
from models.base_model import BaseModel


class City(BaseModel):
    """ A class City that inherits from BaseModel class

    Attributes:
        state_id (str): The id of a state instance
        name (sr): The name of the city
    """
    state_id = " "
    name = " "

    def __init__(self, *args, **kwargs):
        """Initializes an instance"""
        super().__init__(*args, **kwargs)
