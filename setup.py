#!/usr/bin/python

from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
  name="libdiscid",
  version="0.1",
  description="Python bindings of libdiscid",
  author="Sebastian Ramacher",
  author_email="sebastian+dev@ramacher.at",
  url="https://github.com/sebastinas/python-libdiscid",
  license="Expat",
  ext_modules=cythonize([
    Extension("libdiscid.discid",
      [
        "libdiscid/discid.pyx",
        "libdiscid/discid-wrapper.c"
      ]
    )
  ]),
  packages=[
    'libdiscid',
    'libdiscid.tests'
  ],
  install_requires=[
    "cython >= 0.15",
    "setuptools"
  ],
  test_suite="libdiscid.tests",
  use_2to3=True
)
