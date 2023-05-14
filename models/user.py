#!/usr/bin/python3
""" The BaseModel module imported from the models directory """

from models.base_model import BaseModel

"""" A class User that inherits from the BaseModel class """

class User(BaseModel):
""" Public class attributes """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initializing an instance and calling super class """

        super().__init__(*args, **kwargs)
