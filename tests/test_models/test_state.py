#!/usr/bin/python3
"""Test file Storage"""
import unittest
import json
import os
from models.state import State


class TestState(unittest.TestCase):
    """Test State Class"""

    def test_initialization(self):
        """Test initialization"""
        self.assertTrue(hasattr(State, "name"))


if __name__ == '__main__':
    unittest.main()
