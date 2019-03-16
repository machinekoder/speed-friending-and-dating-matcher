# coding=utf-8
from setuptools import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='speed-friending-matcher',
    version='0.1.1',
    packages=['speed_friending_matcher'],
    url='https://github.com/machinekoder/speed-friending-matcher/',
    license='MIT',
    author='Alexander Rössler',
    author_email='alex@machinekoder.com',
    description='Matching software for speed friending events.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['aenum', 'openpyxl', 'pydot', 'flask', 'werkzeug'],
    extras_require={'dev': ['pytest', 'pytest-mock', 'pylint', 'tox']},
    scripts=['bin/speed_friending_matcher'],
    include_package_data=True,
)
