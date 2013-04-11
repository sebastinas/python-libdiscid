#!/usr/bin/python

from setuptools import setup, Extension
# from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
  name="python-libdiscid",
  version="0.1",
  description="Python bindings of libdiscid",
  author="Sebastian Ramacher",
  author_email="sebastian+dev@ramacher.at",
  license="Expat",
  ext_modules=[
    Extension("libdiscid/discid",
      [
        "libdiscid/discid.pyx",
        "libdiscid/discid-wrapper.c"
      ],
      libraries=['discid']
    )
  ],
  packages=[
    'libdiscid',
    'libdiscid.tests'
  ],
  install_requires=[
    "cython >= 0.15",
    "setuptools"
  ],
  test_suite="libdiscid.tests",
  use_2to3=True,
  cmdclass = {
    'build_ext': build_ext
  }
)
