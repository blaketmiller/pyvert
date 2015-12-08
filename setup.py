from setuptools import setup

setup(name='pyvert',
      version='0.2',
      description='pyvert is a tool to convert a filesystem directory structure to and from YAML',
      url='http://github.com/blaketmiller/pyvert',
      author='Blake Miller',
      author_email='blakethomasmiller@gmail.com',
      license='GNU GPL v2.0',
      packages=['pyvert'],
      scripts=['bin/dir2yaml', 'bin/yaml2dir'],
      zip_safe=False)
