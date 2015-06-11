#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import votai_theme

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = votai_theme.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='votai-theme',
    version=version,
    description="""theme for votainteligente instance""",
    long_description=readme + '\n\n' + history,
    author='Felipe Álvarez',
    author_email='falvarez@gmail.com',
    url='https://github.com/lfalvarez/votai-theme',
    packages=[
        'votai_theme',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='votai-theme',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
