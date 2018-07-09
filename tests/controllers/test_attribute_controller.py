# -*- coding: utf-8 -*-

"""
    tests.controllers.test_attribute_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from akkblfpim23.api_helper import APIHelper


class AttributeControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(AttributeControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.attribute

    # Assuming that the given code is the code of an existing attribute
    def test_attribute(self):

        # Perform the API call through the SDK function
        self.controller.get_attribute()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # TODO: Add Description
    def test_attributes(self):

        # Perform the API call through the SDK function
        self.controller.get_attributes()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

