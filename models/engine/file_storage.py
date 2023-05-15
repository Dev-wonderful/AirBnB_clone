#!/usr/bin/python3
"""A module that handles persistence of data"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """A class to handle storage of objects in JSON"""

    __file_path = "file.json"
    __objects = {}
    class_dict = {'Amenity': Amenity,
                  'BaseModel': BaseModel,
                  'City': City,
                  'Place': Place,
                  'Review': Review,
                  'State': State,
                  'User': User}

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
        instance_dict = obj.to_dict()
        key = ".".join([instance_dict['__class__'], instance_dict['id']])
        self.__objects[key] = obj

    def save(self, obj=None):
        """serializes storage dictionary to JSON file"""
        json_obj = {}
        if obj is not None:
            instance_dict = obj.to_dict()
            key = ".".join([instance_dict['__class__'], instance_dict['id']])
            self.__objects[key] = obj
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as json_file:
            json.dump(json_obj, json_file)

    def reload(self):
        """deserializes the JSON file to storage dictionary,
        file path exists
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as json_file:
                objects = json.load(json_file)
            # print("1: {}".format(objects))
            # print("------------------------")
            # print("2: {}".format(self.__objects))
            for key in objects:
                self.__objects[key] = self.reload_instance(objects[key],
                                                           self.class_dict)
        except FileNotFoundError:
            pass

    @staticmethod
    def reload_instance(instance_dict, class_dict):
        class_name = instance_dict['__class__']
        instance = class_dict[class_name](**instance_dict)
        return instance
