libdiscid package
-----------------

:mod:`libdiscid` module
^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: libdiscid
   :members:

.. data:: DEFAULT_DEVICE

  The default device of the platform.

.. deprecated:: 0.2.0
   Use :func:`default_device` instead.

.. data:: FEATURES

  List of available features supported by the current combination of libdiscid
  and platform.

.. data:: FEATURE_READ

  Read the TOC of the disc to get the disc ID. This feature is always enabled.

.. data:: FEATURE_MCN

  Read the Media Catalogue Number of the disc.

.. data:: FEATURE_ISRC

  Read :musicbrainz:`International Standard Recording Codes <ISRC>` of all the
  tracks.

.. data:: __libdiscid_version__

  The version of the underlying libdiscid.

Classes
~~~~~~~

.. autoclass:: libdiscid.DiscId
   :members:

Exceptions
~~~~~~~~~~

.. autoexception:: libdiscid.discid.DiscError
   :show-inheritance:


Subpackages
^^^^^^^^^^^

.. toctree::

   api.compat
