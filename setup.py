#!/usr/bin/env python
import codecs
import os.path

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), "r").read()


install_requires = ["setuptools", "twitter==1.19.2"]

setup(
    name="likesearch",
    description="",
    version="0.1.0",
    long_description=read("README.md"),
    author="",
    url="",
    scripts=["scripts/likesearch"],
    entry_points={"console_scripts": ["likesearch = likesearch:main"]},
    packages=find_packages(exclude=["tests*"]),
    install_requires=install_requires,
    extras_require={},
    python_requires=">= 3.6",
)
