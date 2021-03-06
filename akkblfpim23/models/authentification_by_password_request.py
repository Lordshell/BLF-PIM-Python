# -*- coding: utf-8 -*-

"""
    akkblfpim23.models.authentification_by_password_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class AuthentificationByPasswordRequest(object):

    """Implementation of the 'Authentification by passwordRequest' model.

    TODO: type model description here.

    Attributes:
        username (string): TODO: type description here.
        password (string): TODO: type description here.
        grant_type (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "username":'username',
        "password":'password',
        "grant_type":'grant_type'
    }

    def __init__(self,
                 username=None,
                 password=None,
                 grant_type=None):
        """Constructor for the AuthentificationByPasswordRequest class"""

        # Initialize members of the class
        self.username = username
        self.password = password
        self.grant_type = grant_type


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        username = dictionary.get('username')
        password = dictionary.get('password')
        grant_type = dictionary.get('grant_type')

        # Return an object of this model
        return cls(username,
                   password,
                   grant_type)


