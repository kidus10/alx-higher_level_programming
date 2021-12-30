#!/usr/bin/python3
"""Definition of Rectangle class"""
import json


class Base:
    """Defines a class rectangle.

    Attributes:
        __nb_objects: Width of the rectangle
        id: id of the class

    Args:
        id: id of the class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)
