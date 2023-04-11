#!/usr/bin/python3
""" add_attribute module """


def add_attribute(Object, Name, Value):
    """ add_attribute function """
    if not hasattr(Object, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(Object, Name)):
        Object.__setattr__(Name, Value)
