#!/usr/bin/env python

import os


def to_dir(data, path=str()):
    """
    Return the top-level key of the passed dictionary

    Keyword arguments:
    data -- a dictionary with one top-level key
    path -- a system path as a string
    """

    dest = os.path.join(os.getcwd(), path)

    if isinstance(data, dict):
        for k, v in data.items():
            os.makedirs(os.path.join(dest, k))
            to_dir(v, os.path.join(path, str(k)))

    elif isinstance(data, list):
        for i in data:
            if isinstance(i, dict):
                to_dir(i, path)
            else:
                with open(os.path.join(dest, i), "a"):
                    os.utime(os.path.join(dest, i), None)

    if isinstance(data, dict):
        return list(data.keys())[0]
