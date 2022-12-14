#!/usr/bin/python3
"""Module for Base Class"""


import json
import os


class Base():
    """first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of list_objs to a file"""
        list_dict = []
        if list_objs:
            for i in list_objs:
                list_dict += [i.to_dictionary()]
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON string representation"""
        if json_string is None:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is 'Rectangle':
            obj = cls(3, 9)
        if cls.__name__ is 'Square':
            obj = cls(7)
        obj.update(**dictionary)
        return (obj)

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        return_dict = []
        if os.path.exists(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json", 'r', encoding='utf-8') as f:
                list_dict = cls.from_json_string(f.read())
                for dict in list_dict:
                    return_dict.append(cls.create(**dict))
        return (return_dict)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        list_dict = []
        if list_objs:
            for i in list_objs:
                list_dict += [i.to_dictionary()]
        with open(cls.__name__ + '.csv', 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dict))

    @classmethod
    def load_from_file_csv(cls):
        return_dict = []
        if os.path.exists(cls.__name__ + ".csv"):
            with open(cls.__name__ + ".csv", 'r', encoding='utf-8') as f:
                list_dict = cls.from_json_string(f.read())
                for dict in list_dict:
                    return_dict.append(cls.create(**dict))
        return (return_dict)
