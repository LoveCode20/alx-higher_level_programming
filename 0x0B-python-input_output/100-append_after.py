#!/usr/bin/python3
""" append_after module """


def append_after(filename="", search_string="", new_string=""):
    """ class body. """
    text = " "
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new string
    with open(filename, "n") as w:
        w.write(text)
