#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import lab_student_draft
version = lab_student_draft.__version__

setup(
    name='lab_student_draft',
    version=version,
    author='',
    author_email='jerick@icannhas.com',
    packages=[
        'lab_student_draft',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['lab_student_draft/manage.py'],
)
