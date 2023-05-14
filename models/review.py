#!/usr/bin/python3
""" BaseModel module that is imported from models directory"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ A class Review that inherits from BaseModel

    Attributes:
        place_id (str): id of a Place instance
        user_id (str): id of a User instance
        text (str): the review on the place
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes an instance"""
        super().__init__(*args, **kwargs)
