#!/usr/bin/python3
"""
This module contains BaseModel class
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    This is a base model class
    """
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            self.__create_dict(kwargs)
        else:
            self.id = str(uuid.uuid4())
            time = datetime.now()
            self.created_at = time
            self.updated_at = time
            models.storage.new(self)

    def __create_dict(self, args):
        """
        Creates a new instance from dictionary
        """
        format_dt = "%Y-%m-%dT%H:%M:%S.%f"
        keys = ['id', 'created_at', 'updated_at']
        for key, value in args.items():
            if key in keys:
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, format_dt)
                setattr(self, key, value)

    def __str__(self):
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current time
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        """
        dict = {}
        for key, item in self.__dict__.items():
            dict[key] = item
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
