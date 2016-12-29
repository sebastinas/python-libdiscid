#!/usr/bin/python

import os.path
import sys

from setuptools import setup, Extension

try:
  from Cython.Build import cythonize
  have_cython = True
except ImportError:
  have_cython = False

try:
  import pkgconfig
  have_pkgconfig = True
except ImportError:
  have_pkgconfig = False

if have_pkgconfig and pkgconfig.exists('libdiscid'):
  flags = pkgconfig.parse('libdiscid')
  define_macros = flags['define_macros']
  include_dirs = flags['include_dirs']
  library_dirs = flags['library_dirs']
  libraries = list(flags['libraries'])
else:
  define_macros = ''
  include_dirs = ''
  library_dirs = ''
  libraries = 'discid'

if have_cython:
  # if Cython is available, rebuild _discid.c
  ext = cythonize([
    Extension('libdiscid._discid',
      [
        'libdiscid/_discid.pyx',
        'libdiscid/discid-wrapper.c'
      ],
      define_macros=define_macros,
      include_dirs=include_dirs,
      library_dirs=library_dirs,
      libraries=libraries
    )
  ])
else:
  # ... otherwise use the shipped version of _discid.c
  ext = [
    Extension('libdiscid._discid',
      [
        'libdiscid/_discid.c',
        'libdiscid/discid-wrapper.c'
      ],
      define_macros=define_macros,
      include_dirs=include_dirs,
      library_dirs=library_dirs,
      libraries=libraries
    )
  ]

setup_requires = ['pkgconfig']
if have_cython:
  # if Cython is available, check if it's new enough
  setup_requires.append('cython >= 0.15')

def read(name):
  f = open(os.path.join(os.path.dirname(__file__), name))
  ret = f.read()
  f.close()
  return ret

setup(
  name='python-libdiscid',
  version='1.0',
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
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Ripping',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],
  test_suite='libdiscid.tests',
  setup_requires=setup_requires
)
