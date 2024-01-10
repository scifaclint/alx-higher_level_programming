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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        return self.__dict__
