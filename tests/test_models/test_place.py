#!/usr/bin/python3
"""Test file Storage"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test Place Class"""

    def test_initialization(self):
        """Test initialization"""
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))


if __name__ == '__main__':
    unittest.main()
