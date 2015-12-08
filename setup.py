from setuptools import setup


def readme():
    with open('README.rst', 'r') as f:
        return f.read()

setup(name='pyvert',
      version='0.3',
      description='pyvert is a tool to convert a filesystem directory structure to and from YAML',
      long_description=readme(),
      classifiers=['Intended Audience :: Developers',
                   'Intended Audience :: Information Technology',
                   'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Software Development :: Testing',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: System :: Filesystems',
                   'Topic :: System :: Archiving',
                   'Topic :: Utilities'],
      keywords='convert folder file dictionary yaml structure filesystem represent utility',
      url='http://github.com/blaketmiller/pyvert',
      author='Blake Miller',
      author_email='blakethomasmiller@gmail.com',
      license='GNU GPL v2.0',
      packages=['pyvert'],
      install_requires=['pyyaml'],
      scripts=['bin/dir2yaml', 'bin/yaml2dir'],
      zip_safe=False)
