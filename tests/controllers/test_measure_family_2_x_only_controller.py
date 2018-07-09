# -*- coding: utf-8 -*-

"""
    tests.controllers.test_measure_family_2_x_only_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from akkblfpim23.api_helper import APIHelper


class MeasureFamily2XOnlyControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(MeasureFamily2XOnlyControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.measure_family_2_x_only

    # Assuming that the given code is the code of an existing measure family
    def test_measure_family_2_x_only(self):

        # Perform the API call through the SDK function
        self.controller.get_measure_family_2_x_only()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # TODO: Add Description
    def test_measure_families_2_x_only(self):

        # Perform the API call through the SDK function
        self.controller.get_measure_families_2_x_only()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
