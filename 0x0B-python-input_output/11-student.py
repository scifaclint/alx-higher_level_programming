#!/usr/bin/python3
"""
This module contains a class Student that defines a student by:
    Public instance attributes:
        first_name
        last_name
        age
"""


class Student:
    """
    A class that defines a student by:
    Public instance attributes:
        first_name
        last_name
        age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings representing the attribute names
            that should be retrieved.
            If it's None or not a list, all attribute names are retrieved.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            return {
                    attr: getattr(self, attr)
                    for attr in attrs
                    if type(attr) is str and hasattr(self, attr)
                    }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary with attribute names as keys and the
            corresponding attribute values as values.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
