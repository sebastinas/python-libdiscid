API documentation
-----------------

.. automodule:: libdiscid
   :members:

.. data:: DEFAULT_DEVICE

  The default device of the platform.

.. data:: FEATURES

  List of available features supported by the current combination of libdiscid
  and platform.

.. data:: FEATURE_MCN

  Read the Media Catalogue Number of the disc.

.. data:: FEATURE_ISRC

  Read :musicbrainz:`International Standard Recording Codes <ISRC>` of all the
  tracks.

.. data:: __libdiscid_version__

  The version of the underlying libdiscid.

Classes
^^^^^^^

.. autoclass:: libdiscid.DiscId
   :members:

Exceptions
^^^^^^^^^^

.. autoexception:: libdiscid.discid.DiscError
   :show-inheritance:
