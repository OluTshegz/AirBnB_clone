#!/usr/bin/python3
"""This city module contains City class and imports class BaseModel class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city in the application.

    Attributes:
        state_id (str): The ID of the state the city belongs to.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
