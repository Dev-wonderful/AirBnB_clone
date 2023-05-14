#!/usr/bin/python3
""" A BaseModel module that is imported from models directory"""
from models.base_model import BaseModel


class State(BaseModel):
    """ A class State that inherits from the BaseModel

    Attributes:
        name (str): name of the state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes an instance"""
        super().__init__(*args, **kwargs)
