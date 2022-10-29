#!/usr/bin/python3
"""
This runs unittests for base_model file
"""
import unittest
from models.base_model import BaseModel
import os
import pep8


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

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")

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

    def test_kwargs(self):
        """
        Testing Kwargs with initialization 
        """
        b = BaseModel()
        self.assertEqual(type(b).__name__, "BaseModel")
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, 'updated_at'))
        self.assertTrue(hasattr(b, "__class__"))

if __name__ == "__main__":
    unittest.main()
