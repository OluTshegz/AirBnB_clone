#!/usr/bin/python3
"""This state module contains State class and imports class BaseModel class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state in the application.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
