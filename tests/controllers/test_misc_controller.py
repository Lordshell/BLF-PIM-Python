# -*- coding: utf-8 -*-

"""
    tests.controllers.test_misc_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from akkblfpim23.api_helper import APIHelper
from akkblfpim23.models.authentification_by_password_request import AuthentificationByPasswordRequest
from akkblfpim23.models.authentification_by_refresh_token_request import AuthentificationByRefreshTokenRequest


class MiscControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(MiscControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.misc

    # TODO: Add Description
    def test_authentification_by_password(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"username":"{{username}}","password":"{{password}}","grant_type":"password"}', AuthentificationByPasswordRequest.from_dictionary)
        content_type = 'application/json'

        # Perform the API call through the SDK function
        self.controller.create_authentification_by_password(body, content_type)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

    # TODO: Add Description
    def test_authentification_by_refresh_token(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"refresh_token":"{{refreshToken}}","grant_type":"refresh_token"}', AuthentificationByRefreshTokenRequest.from_dictionary)
        content_type = 'application/json'

        # Perform the API call through the SDK function
        self.controller.create_authentification_by_refresh_token(body, content_type)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

