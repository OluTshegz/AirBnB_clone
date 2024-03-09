#!/usr/bin/python3

"""
Module-level documentation for the script.

This script imports necessary modules and
packages required for the application.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class for all models in the application.

    Attributes:
        id (str): The unique identifier for the instance.
        created_at (datetime): The timestamp of when
            the instance was created.
        updated_at (datetime): The timestamp of when
            the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Note:
            If kwargs is not empty, the instance will be initialized with the
            provided attributes. Otherwise, a new instance will be created with
            a unique id and current timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        # Corrected indentation for the line below
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Updates the updated_at timestamp and saves the instance to the storage.

        Note:
            This method updates the updated_at
            attribute to the current timestamp
            and then saves the instance to the storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: A dictionary containing the instance attributes.

        Note:
            This method converts the instance
            attributes to a dictionary format,
            including class name and timestamp attributes in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A string containing class name, id, and attribute dictionary.

        Note:
            This method provides a human-readable string representation of the
            instance, including class name, id, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
