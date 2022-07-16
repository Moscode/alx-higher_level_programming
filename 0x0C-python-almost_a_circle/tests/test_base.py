#!/usr/bin/python3


import unittest

from models.base import Base

class TestBaseClassInstantiation(unittest.TestCase):
    def test_has_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b1.id + 1)

    def test_has_arg(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
