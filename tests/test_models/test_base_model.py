#!/usr/bin/python3
""" module containts unittests for class BaseModel """


import unittest
import json
from models.base_model import BaseModel

class testBaseModel(unittest.TestCase):
    """ unittests for BaseModel """

    def setUp(self):
        """ Sets up the class """
        self.basemodel = BaseModel()

    def tearDown(self):
        """ Test for tear down """
        del self.basemodel

    def testId(self):
        """ Tests id """

    def test_created_at(self):
        """ Datetime at creation of an object """

    def test_updated_at(self):
        """ Datetime at update of an object """

    def test_str(self):
        """ Test that str prints details correctly """

    def test_to_dict(self):
        """ Test that keys/values are saving correctly """

    def test_save(self):
        """ Tests that instance attributes are saved and updated
        correctly with the proper updated datetime """


if __name__ == "__main__":
    testBaseModel()