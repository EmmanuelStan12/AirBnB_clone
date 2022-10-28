#!/usr/bin/env python3
import uuid
import datetime
"""
This module contains BaseModel class
"""

class BaseModel:
    """
    This is a base model class
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        time = datetime.datetime.now()
        self.created_at = time
        self.updated_at = time

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current time
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        """
        dict = self.__dict__
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
