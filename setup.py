#!/usr/bin/python

from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
  name="libdiscid",
  version="0.1",
  description="Python binding of libdiscid",
  author="Sebastian Ramacher",
  author_email="sebastian+dev@ramacher.at",
  license="Expat",
  ext_modules = cythonize([
    Extension("libdiscid", ["discid.pyx", "discid-wrapper.c"])
  ]),
  install_requires = [
    "cython",
    "setuptools"
  ]
)
