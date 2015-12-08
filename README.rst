pyvert
======

Pyvert is a tool to convert a filesystem directory structure to and from YAML. Comes in useful for development when a directory of test files and folders is desired.


Modules
-------
For converting a directory to a dict, use convert_dir:

.. code-block:: python

    >>> from pyvert import convert_dir
    >>> foo = convert_dir.to_dict("/path/to/directory")
    >>> type(foo)
    <type 'dict'>


Scripts
-------
From command line, generate a YAML file of a given directory:

.. code-block:: bash

    $ dir2yaml /path/to/foobar
    Dictionary written to foobar.yaml

Also works in reverse:

.. code-block:: bash

    $ yaml2dir foobar.yaml
    Directory created at /path/to/foobar


Installation
------------
To install Pyvert, simply:

.. code-block:: bash

    $ pip install pyvert
