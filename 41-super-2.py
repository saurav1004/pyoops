#!/usr/bin/env python

# 41-super-2.py



import abc


class MyClass(object):

    __metaclass__ = abc.ABCMeta

    def my_set_val(self, value):
        self.value = value

    def my_get_val(self):
        return self.value

    @abc.abstractmethod
    def print_doc(self):
        return


class MyChildClass(MyClass):
    def my_set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(MyChildClass, self).my_set_val(self)

    def print_doc(self):
        print("Documentation for MyChild Class")


my_instance = MyChildClass()
my_instance.my_set_val(100)
print(my_instance.my_get_val())
my_instance.print_doc()
