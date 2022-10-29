#!/usr/bin/python3
"""Test file Storage"""
import unittest
import json
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test State Class"""

    def test_initialization(self):
        """Test initialization"""
        self.assertTrue(hasattr(Amenity, "name"))


if __name__ == '__main__':
    unittest.main()
