#!/usr/bin/env python

import glob
import os
import sys

from setuptools import find_packages, setup


def read(fname):
    """Read the contents of a file.

    Args:
        fname: path to file.

    Returns:
        the file contents.
    """
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name="AcmeInstrumentsService",
    version="0.1.dev0",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    python_requires=">=3.6",
    install_requires=read("requirements.txt").splitlines(),
    author="IBM Quantum team",
    author_email="juan.gomez.mosquera1@ibm.com",
    description="REST Service for using quantum computer instruemnt controllers",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/atilag/AcmeInstrumentsService",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
