#!/usr/bin/python

import os.path
import sys

try:
  from setuptools import setup, Extension
  have_setuptools = True
except ImportError:
  from distutils.core import setup
  from distutils.extension import Extension
  have_setuptools = False

try:
  from Cython.Build import cythonize
  have_cython = True
except ImportError:
  have_cython = False

if have_cython:
  # if Cython is available, rebuild _discid.c
  ext = cythonize([
    Extension('libdiscid._discid',
      [
        'libdiscid/_discid.pyx',
        'libdiscid/discid-wrapper.c'
      ]
    )
  ])
else:
  # ... otherwise use the shipped version of _discid.c
  ext = [
    Extension('libdiscid._discid',
      [
        'libdiscid/_discid.c',
        'libdiscid/discid-wrapper.c'
      ]
    )
  ]

if have_setuptools:
  tests_require = []
  if sys.version_info[0:2] < (2,7):
    tests_require = ['unittest2']

  args = {
    'test_suite': 'libdiscid.tests',
    'tests_require': tests_require,
  }

  if have_cython:
    # if Cython is available, check if it's new enough
    args['setup_requires'] = ['cython >= 0.15']
else:
  args = {}

def read(name):
  f = open(os.path.join(os.path.dirname(__file__), name))
  ret = f.read()
  f.close()
  return ret

setup(
  name='python-libdiscid',
  version='0.4.1',
  description='Python bindings for libdiscid',
  long_description=read('README.rst'),
  author='Sebastian Ramacher',
  author_email='sebastian+dev@ramacher.at',
  url='https://github.com/sebastinas/python-libdiscid',
  license='Expat',
  ext_modules=ext,
  packages=[
    'libdiscid',
    'libdiscid.tests',
    'libdiscid.compat'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Ripping',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],
  **args
)
