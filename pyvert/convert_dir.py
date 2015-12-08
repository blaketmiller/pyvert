#!/usr/bin/env python

import os


def to_dict(path):
    """
    Return the dictionary created by recursively walking directory

    Keyword arguments:
    path -- a system path as a string
    """

    directory = {}

    for dirname, dirnames, filenames in os.walk(path):
        dn = os.path.basename(dirname)
        directory[dn] = []

        if dirnames:
            for d in dirnames:
                directory[dn].append(to_dict(path=os.path.join(path, d)))

            for f in filenames:
                directory[dn].append(f)
        else:
            directory[dn] = filenames

        return directory
