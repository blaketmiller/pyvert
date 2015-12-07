#!/usr/bin/env python

import os
import sys
import yaml


def dict_to_dir(data, path=str()):
    """dict_to_dir expects data to be a dictionary with one top-level key."""

    dest = os.path.join(os.getcwd(), path)

    if isinstance(data, dict):
        for k, v in data.items():
            os.makedirs(os.path.join(dest, k))
            dict_to_dir(v, os.path.join(path, str(k)))

    elif isinstance(data, list):
        for i in data:
            if isinstance(i, dict):
                dict_to_dir(i, path)
            else:
                with open(os.path.join(dest, i), "a"):
                    os.utime(os.path.join(dest, i), None)

    if isinstance(data, dict):
        return list(data.keys())[0]

if len(sys.argv) == 1:
    sys.stderr.write("Too few arguments\n")
    sys.exit(1)
elif len(sys.argv) == 2:
    y = os.path.abspath(sys.argv[1])
    p = str()
elif len(sys.argv) == 3:
    y = os.path.abspath(sys.argv[1])
    p = os.path.abspath(sys.argv[2])
else:
    sys.stderr.write("Unexpected argument {}\n".format(sys.argv[3:]))
    sys.exit(1)

try:
    with open(y, "r") as f:
        try:
            d = yaml.load(f)
            dest = dict_to_dir(data=d, path=p)
            print("Directory created at {}".format(p if p else os.path.join(os.getcwd(), dest)))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)
