# Changelog

## 2.0.2 (2022-11-01)

  * Remove long deprecated `libdiscid.DEFAULT_DEVICE`.
  * Bump required Python version to 3.7.

## 2.0.1 (2021-02-11)

  * Fix `python_requires` in setup.cfg.
    A typo caused the information not to be included in PKG-INFO.

## 2.0 (2021-02-10)

  * Remove `compat` module for the 0.x style interface.
  * Add type annotations.

  * Internal changes:
    - Modernize build system: move build dependencies to `pyproject.toml`.
    - Use relative imports

## 1.2 (2021-01-24)

  * Bump required Python version to 3.6.
  * Replaced use of `unicode` with `str`.

## 1.1 (2019-11-10)

  * Remove support for Python 2.
  * Note Fedora package availability. Thanks to Ville Skyttä.
  * Fix the build without `pkgconfig` module. Thanks to Philipp Wolfer.

## 1.0 (2016-12-29)

  * Fix compatibility issues with Cython 0.23.
  * Add support for Python 3.4, 3.5, and 3.6.
  * Drop (active) support for Python 2.6, 3.2 and 3.3. This change only
    affects the test suite.
  * Fix various spelling mistakes.

  * Internal changes:
    - Use `pkgconfig` to detect discid.
    - Use Travis-CI.

## 0.4.1 (2014-01-03)

  * Fix typo in `test_read_not_implemented` test.
  * `libdiscid.compat.discid`: Add `toc_string property` for compatibility with
    python-discid 1.1.0. Thanks to Johannes Dewender.

  * Internal changes:
    - Move test data to common location for deduplication.

## 0.4 (2013-10-03)

  * Add support for libdiscid's `discid_get_toc_string` introduced in 0.6.0.
  * Add sectors_to_seconds to libdiscid.
  * Use shipped C source to build `libdiscid._discid` if Cython is not available.

  * Internal changes:
    - Release resources acquired from libdiscid earlier. After a successful
      read or put all the information is stored in the returned object and no
      further calls to libdiscid are necessary to access the data.

## 0.3.1 (2013-09-09)

  * Fix handling of `None` in `libdiscid.compat.discid.read`.

## 0.3 (2013-07-04)

  * The device used to read the data is now stored in `DiscId`'s device
    property.
  * Make `DiscError` available as `libdiscid.DiscError`.
  * `libdiscid.compat.discid`:
    - Fix features handling.
    - Try to decode devices with the filesystem's encoding and features with
      ascii on a best effort basis.
    - Thanks to Andreas Stührk for the hints.

  * Internal changes:
    - Move most of the API documentation from the rst files back to the code.
    - Name the extension module as `libdiscid._discid` and move some bits that
      don't require Cython away.

## 0.2.0 (2013-06-30)

  * Add `libdiscid.compat.discid` module that provides the same interface as the
    `discid` module from python-discid. This allows devlopers to write
    applications that work with both python-libdiscid and python-discid
    without much effort.
  * Deprecate `libdiscid.DEFAULT_DEVICE` in favor of `libdiscid.default_device`.
    The default device might change one some platforms during the runtime, so
    it should not be a constant.

## 0.1.2 (2013-05-09)

  * Fix issues with Cython 0.19.
  * Don't fail tests if MCN or ISCR is not available on the platform.

## 0.1.1 (2013-04-3)

  * Fix issues with symbol names if python-libdiscid was built against
    a libdiscid version prior to 0.5.0 and then used with 0.5.0.

## 0.1 (2013-04-11)

  * Initial release.
