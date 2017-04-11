#!/usr/bin/env python
from setuptools import setup, find_packages
from cah import VERSION

# Donload question/answer data:
from cah.data import download

setup(name='python-cah',
      version=VERSION,
      description='A Cards Against Humanity game framework',
      author='Lucien Gaitskell',
      url='https://github.com/luciengaitskell',
      package_data={'': ['data/bin/*.txt']},
      packages=find_packages()
     )
