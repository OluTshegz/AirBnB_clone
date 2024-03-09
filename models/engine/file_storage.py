#!/usr/bin/python3

"""
Imports necessary modules and classes for the application.

This script imports the following modules and classes:
- json: Provides functions for encoding and decoding JSON data.
- BaseModel: The base class for all models in the application.
- User: Represents a user in the application.
- State: Represents a state in the application.
- City: Represents a city in the application.
- Amenity: Represents an amenity in the application.
- Place: Represents a place in the application.
- Review: Represents a review in the application.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class for managing storage operations using JSON files.

    Attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): A dictionary containing serialized objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves all objects from the storage.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: The object to be added to the storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Saves the objects in the storage to the JSON file.
        """
        serialized_obj_dict = {}
        for key, value in self.__objects.items():
            serialized_obj_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_obj_dict, file, indent=4)

    def reload(self):
        """
        Loads objects from the JSON file into the storage.
        """
        try:
            with open(self.__file_path, "r") as file:
                deserialized_obj_dict = json.load(file)
                for key, value_obj_dict in deserialized_obj_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "User":
                        self.__objects[key] = User(**value_obj_dict)
                    elif class_name == "State":
                        self.__objects[key] = State(**value_obj_dict)
                    elif class_name == "City":
                        self.__objects[key] = City(**value_obj_dict)
                    elif class_name == "Amenity":
                        self.__objects[key] = Amenity(**value_obj_dict)
                    elif class_name == "Place":
                        self.__objects[key] = Place(**value_obj_dict)
                    elif class_name == "Review":
                        self.__objects[key] = Review(**value_obj_dict)
                    else:
                        _class_name_ = eval(value_obj_dict["__class__"])
                        self.__objects[key] = _class_name_(**value_obj_dict)
        except FileNotFoundError:
            pass

    def classes(self):
        """
        Returns a dictionary of available classes.

        Returns:
            dict: A dictionary containing available classes.
        """
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        return classes
