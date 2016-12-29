Miscellaneous
-------------

Bugs
^^^^

Please report bugs to the project's issue tracker at `GitHub`_.

Supported libdiscid features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`python-libdiscid` supports all the features introduced by `libdiscid` up to
version 0.6.0, that is:

* retrieval of the disc's Media Catalogue Number and retrieving the
  :musicbrainz:`International Standard Recording Code <ISRC>` of
  the tracks if you are using `libdiscid` 0.4.0 and above.
* selective reading support if you are using `libdiscid` 0.5.0 and above.
* fuzzy TOC lookup if you are using `libdiscid` 0.6.0 and above.

Please note that if `python-libdiscid` was built against versions of `libdiscid`
prior to 0.4.0 or 0.5.0, `python-libdiscid` has to be rebuilt against the newer
version to detect the features of the newer `libdiscid`.

Other Python bindings
^^^^^^^^^^^^^^^^^^^^^

There are other Python bindings available. `python-discid`__ is the most
prominent one. For a full list of bindings (including bindings for other
languages) check musicbrainz:`libdiscid`.

.. _GitHub: https://github.com/sebastinas/python-libdiscid
.. __: https://github.com/JonnyJD/python-discid
