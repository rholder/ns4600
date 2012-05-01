#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

settings = dict()


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

settings.update(
    name='ns4600',
    version='1.0.0',
    description='Control the Promise SmartStor NS4600 NAS server',
    long_description=open('README.rst').read(),
    author='Ray Holder',
    url='https://github.com/rholder/ns4600',
    py_modules= ['ns4600'],
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    )
)


setup(**settings)
