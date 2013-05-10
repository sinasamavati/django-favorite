#!/usr/bin/env python

import os
from setuptools import setup


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).readlines()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-favorite',
    version='0.0.1',
    packages=['favorite'],
    include_package_data=True,
    license='MIT License',
    description=README[2].rstrip('\n'),
    long_description=''.join(README),
    url='https://github.com/s1n4/django-favorite',
    author='Sina Samavati',
    author_email='sina.samv@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    )
