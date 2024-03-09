#!/usr/bin/python3
"""This review module contains Review class
and imports class BaseModel class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review in the application.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
