#!/usr/bin/python3
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self,name):
        return self.__name

    @property
    def age(self, age):
        return self.__age

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    def print_person(self):
        print(f"My name is {self.__name} and I am {self.__age} years old")
    
person1 = Person("Klaus", 30)
person2 = Person("Donaldo", 11)
person3 = Person("Fatjoni", 2)

personlist = [person1, person2, person3]
for el in personlist:
    el.print_person()

