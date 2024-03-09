#!/usr/bin/python3
"""This amenity module contains Amenity class
and imports class BaseModel class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity in the application.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
