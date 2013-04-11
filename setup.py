#!/usr/bin/python

from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
  name="python-libdiscid",
  version="0.1",
  description="Python binding of libdiscid",
  author="Sebastian Ramacher",
  author_email="sebastian+dev@ramacher.at",
  license="Expat",
  ext_modules = cythonize([
    Extension("libdiscid/discid", [
        "libdiscid/discid.pyx",
        "libdiscid/discid-wrapper.c"
    ])
  ]),
  packages = ['libdiscid'],
  install_requires = [
    "cython >= 0.15",
    "setuptools"
  ]
)
