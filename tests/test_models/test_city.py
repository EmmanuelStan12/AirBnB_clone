#!/usr/bin/python3
"""Test file Storage"""
import unittest
import json
import os
from models.city import City


class TestCity(unittest.TestCase):
    """Test State Class"""

    def test_initialization(self):
        """Test initialization"""
        self.assertTrue(hasattr(City, "name"))


if __name__ == '__main__':
    unittest.main()
