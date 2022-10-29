#!/usr/bin/python3
"""
This file contains the file storage class
"""
from json import dump, load, dumps
from os.path import exists
from models import base_model


BaseModel = base_model.BaseModel

class FileStorage:
    """
    This is a file storage class
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
        Returns the dictionary objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj.class>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            dump(dict_to_json, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        dict_obj = {}
        class_names = ["BaseModel"]
        FileStorage.__objects = {}
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r') as f:
                dict_obj = load(f)
                for key, value in dict_obj.items():
                    class_name = key.split('.')[0]
                    if class_name in class_names:
                        FileStorage.__objects[key] = eval(class_name)(**value)
