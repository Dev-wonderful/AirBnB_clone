#!/usr/bin/python3
""" A module to specify the base class"""
import models
from datetime import datetime
import uuid


class BaseModel:
    """The BaseModel class to be inherited"""

    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel class instance

        Args:
            kwargs: To reload an existing instance using a dictionary
        """
        if bool(kwargs):
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """User-friendly information of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the self.updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save(self)

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        instance_dict = {**self.__dict__,
                         '__class__': self.__class__.__name__,
                         'created_at': self.created_at.isoformat(),
                         'updated_at': self.updated_at.isoformat()}
        return instance_dict
