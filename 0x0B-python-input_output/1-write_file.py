#!/usr/bin/pthon3
""" write_file module. """


def write_file(filename="", text=""):
    """ write a string to a UTF8 text file. """
    with open(filename, w="", encoding="UTF-8") as my_file:
        return my_file.write(text)
