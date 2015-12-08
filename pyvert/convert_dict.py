#!/usr/bin/env python

import os


def to_dir(data, path=str()):
    """dict_to_dir expects data to be a dictionary with one top-level key."""

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
