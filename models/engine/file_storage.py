#!/usr/bin/python3
"""A module that handles persistance of data"""
import json


class FileStorage:
    """A class to handle storage of objects in JSON"""

    __file_path: str
    __objects: dict = {}

    def __init__(self):
        """Initializes an instance of this class"""
        pass

    def all(self):
        """returns the storage dictionary of objects"""
        return __objects

    def new(self, obj):
        """adds a new object to the storage dictionary of objects
        Args:
            obj (obj): The object to be added
        """
        key = ".".join([(obj.__clas__.__name__), obj.id])
        __object[key] = obj.to_dict()

    def save(self):
        """serializes storage dictionary to JSON file"""
        with open(__file_path, 'w', encoding="utf-8") as json_file:
            json.dump(__objects, json_file)

    def reload(self):
        """deserializes the JSON file to storage dictionary, file path exists"""
        with open(__file_path, 'r', encoding="utf-8") as json_file:
            json.load(json_file)

