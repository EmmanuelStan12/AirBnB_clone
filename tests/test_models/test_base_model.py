#!/usr/bin/env python3
"""
This runs unittests for base_model file
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    This tests the Base model class
    """

    def test_initialization(self):
        """
        Tests the initialization of the base class
        """
        b = BaseModel()
        self.assertNotEqual(self.id, None)
        self.assertEqual(b.created_at, b.updated_at)

    def test_initialization_with_dictionary(self):
        """
        Tests the initialization with dictionary
        """
        b = BaseModel()
        d = b.to_dict()
        b2 = BaseModel(**d)
        self.assertEqual(str(b), str(b2))



    def test_str(self):
        """
        Tests the return of a string
        """
        b = BaseModel()
        result = "[{}] ({}) {}".format(b.__class__.__name__, b.id, b.__dict__)
        self.assertEqual(str(b), result)

    def test_save(self):
        """
        Tests the save of the base model
        """
        b = BaseModel()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_to_dict(self):
        """
        Tests the 'to dictionary function' for all keys and values
        """
        b = BaseModel()
        dict = b.to_dict()
        result = "{'__class__': 'BaseModel', 'updated_at': '{}', 'created_at': '{}', 'id': '{}'}".format(b.updated_at, b.created_at, b.id)
        self.assertEqual(str(dict), result)
