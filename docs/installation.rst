Installation
------------

Dependencies
^^^^^^^^^^^^

`python-libdiscid` depends on the following components:

* :musicbrainz:`libdiscid`
* `Cython`__ (>= 0.15)
* `pkgconfig`__

Note that `Cython` is only required if one builds `python-libdiscid` from the
repository. The released tarballs ship with pre-built C source files for the
extension mdoules.

If `pkgconfig` is installed, `setup.py` uses `libdiscid`'s `pkg-config`
information to set include directories, libraries to link, etc.

On Debian based systems, the dependencies are only an `apt-get` away::

 apt-get install cython libdiscid-dev python-pkgconfig

`Cython` and `pkgconfig` are also available via `PyPI`__::

 pip install cython
 pip install pkgconfig

.. __: http://www.cython.org/
.. __: https://github.com/matze/pkgconfig
.. __: https://pypi.python.org

Known supported distributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`python-libdiscid` is available in some distributions:

* `Debian <http://packages.debian.org/en/source/sid/python-libdiscid>`_
* `Ubuntu <https://launchpad.net/ubuntu/+source/python-libdiscid>`_

PyPI
^^^^

`python-libdiscid` is available from `PyPI`__::

 pip install python-libdiscid

You can also download the tarball from `PyPI`__ manually, unpack
it and run::

 python setup.py install

A note for Windows users
~~~~~~~~~~~~~~~~~~~~~~~~

There are eggs available from the same source too. With these eggs, the
extension module comes pre-built. However, you still need to fetch
`discid.dll` from :musicbrainz:`libdiscid` and copy the DLL to somewhere it can
be found, e.g. to ``C:\WINDOWS\system32``.

.. __: https://pypi.python.org/pypi/python-libdiscid/
.. __: https://pypi.python.org/pypi/python-libdiscid/

Building python-libdiscid locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you just want to try `python-libdiscid` without installing, please note that
per default `setuptools` will build the extension module in ``build/lib.*`` and
doesn't copy it to ``libdiscid``. There are many possible ways to work with this
limitation:

* Running::

   python setup.py build_ext -i

  will copy the extension modules to ``libdiscid`` and one can hack right away.

* Use `setuptools` ``develop`` command. Please read `setuptools`'s
  `documentation`__ for further information.

* If you build with ``python setup.py build``, It is also possible to put
  ``build/lib.*`` before the source directory of `python-libdiscid` in
  ``sys.path``. Assuming that `python-libdiscid` is built on a 64 bit Linux and
  for `Python` 3.4, one can use the following lines to achieve that::

    import sys, os
    sys.path.insert(0, os.path.abspath('build/lib.linux-x86_64-3.4'))
    import libdiscid

  Please note that modification to any file in the ``libdiscid`` directory will
  only be available after another run of ``python setup.py build``.

.. __: http://pythonhosted.org/distribute/setuptools.html#development-mode
