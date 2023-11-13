#!/usr/bin/python3

import json

class Base:
    """
    Base class for managing id attribute in all classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int, optional): Identifier of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation.
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries represented by json_string.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List of dictionaries.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes set using the update method.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Instance: Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in dictionaries]
                return instances
        except FileNotFoundError:
            return []
