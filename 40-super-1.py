#!/usr/bin/env python

# 40-super-1.py

# This is an example on how super() works
# in Inheritance.

# Reference: https://www.python-course.eu/python3_inheritance.php
# super() is a built-in function that returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class.
# In Python, super() has two major use cases:
# Allows us to avoid using base class explicitly
# Working with Multiple Inheritance 



class MyClass(object):
    def func(self):
        print("I'm being called from the Parent class")


class ChildClass(MyClass):
    def func(self):
        print("I'm actually being called from the Child class")
        print("But...")
        # Calling the `func()` method from the Parent class.
        super(ChildClass, self).func()


my_instance_2 = ChildClass()
my_instance_2.func()
