#!/usr/bin/env python

from setuptools import setup, find_packages

# hack to fix a Python 2.7.3 issue with multiprocessing module --
# see http://bugs.python.org/issue15881
# pylint: disable=unused-import
try:
    import multiprocessing
except ImportError:
    pass

dependencies = [
    # packages for which we want latest stable version
    "pep8>=1.5.6",
    "pylint>=1.2.1",
    "ipython>=2.0.0",
    "uwsgi>=2.0.4",
    # Flask and extensions
    "flask==0.10.1",
    "flask-script==2.0.5",
    "flask-webtest==0.0.7",
    # Additional packages
    "pytest==2.6.4",
    "pytest-cov==1.8.1",
    "sqlalchemy==0.9.8",
    "webtest==2.0.15"
]

setup(
    name="flask-api-skeleton",
    version="0.1",
    url="https://github.com/nezaj/flask-api-skeleton",
    packages=find_packages(),
    install_requires=dependencies
)
