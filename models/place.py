#!/usr/bin/python3
""" BaseModel module imported from models directory"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ A class Place that inherits from BaseModel

    Attributes:
        city_id (str): id of a city instance
        user_id (str): id of a user instance
        name (str): name of the place
        description (str): the description of this place
        number_rooms (int): number of rooms at this place
        number_bathrooms (int): number of bathrooms present at this place
        max_guest (int): maximum guests allowed
        price_by_night (int): night price
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (list): list of all the amenity ids present at this place
    """
    city_id = " "
    user_id = " "
    name = " "
    description = " "
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initializes an instance"""
        super().__init__(*args, **kwargs)
