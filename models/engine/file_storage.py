#!/usr/bin/python3
"""A module that handles persistance of data"""


class FileStorage:
    """A class to handle storage of objects in JSON"""

    __file_path: str
    __objects: dict = {}

    def __init__(self):
        """Initializes an instance of this class"""
        pass

    def all(self):
        """returns the dictionary of objects"""
        return __objects

    def new(self, obj):
        """set"""
