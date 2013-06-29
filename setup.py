#!/usr/bin/python

import os.path
import sys
from setuptools import setup, Extension
from Cython.Build import cythonize

test_requires=[]
if sys.version_info[0:2] < (2,7):
  test_requires=["unittest2"]

def read(name):
  f = open(os.path.join(os.path.dirname(__file__), name))
  ret = f.read()
  f.close()
  return ret

setup(
  name="python-libdiscid",
  version="0.2.0",
  description="Python bindings for libdiscid",
  long_description=read("README.rst"),
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
    'libdiscid.tests',
    'libdiscid.compat'
  ],
  install_requires=[
    "cython >= 0.15",
    "setuptools"
  ],
  test_suite="libdiscid.tests",
  tests_require=test_requires,
  use_2to3=True,
  classifiers=[
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Ripping",
    "Topic :: Software Development :: Libraries :: Python Modules"
  ]
)
