#!/usr/bin/python3
"""A module that handles persistance of data"""
import json


class FileStorage:
    """A class to handle storage of objects in JSON"""

    __file_path = "file.json"
    __objects= {}

    def __init__(self):
        """Initializes an instance of this class"""
        pass

    def all(self):
        """returns the storage dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """adds a new object to the storage dictionary of objects
        Args:
            obj (obj): The object to be added
        """
        key = ".".join([obj['__class__'], obj['id']])
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes storage dictionary to JSON file"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """deserializes the JSON file to storage dictionary, file path exists"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as json_file:
                FileStorage.__objects = json.load(json_file)
        except FileNotFoundError:
            pass

    def user(self):

