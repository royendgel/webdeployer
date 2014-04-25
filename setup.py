import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
readme = open('README.md').read()
setup(
    name = "deployer",
    version = "0.0.1",
    author = "Royendgel Silberie",
    author_email = "royendgel@techprocur.com",
    description = ("Personal Deployer for site created with Flask and Django"),
    keywords = "deployer automation fabric",
    url = "https://github.com/royendgel",
    packages=[''],
    long_description=read('README.md'),
    classifiers=[
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: Unix',
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'Programming Language :: Python :: 2.7',
    ],
)