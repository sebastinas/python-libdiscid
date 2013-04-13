Miscellaneous
-------------

Bugs
^^^^

Please report bugs to the project's issue tracker at `GitHub`_.

libdiscid features support
^^^^^^^^^^^^^^^^^^^^^^^^^^

`python-libdiscid` supports all the features introduced by `libdiscid` up to
version 0.5.0, meaning:

* Retrieval of the disc's Media Catalogue Number and retrieving the
  :musicbrainz:`International Standard Recording Code <ISRC>` of
  the tracks if you're using `libdiscid` 0.4.0 and above.
* Selective reading support if you're using `libdiscid` 0.5.0 and above.

Please note that if `python-libdiscid` was built against versions of `libdiscid`
prior to 0.4.0 or 0.5.0, `python-libdiscid` has to be rebuilt against the newer
version to detect the features of the newer `libdiscid`.

Other Python bindings
^^^^^^^^^^^^^^^^^^^^^

There are other Python bindings available. For a full list of bindings check
:musicbrainz:`libdiscid`.

Note that there are similarities between `python-libdiscid` and
`python-discid`__. However, there are subtle differences:

* `python-discid` follows the typical usage of `libdiscid`'s API more closely::

    from discid import DiscId
    # with with statement
    with DiscId() as disc:
      disc.read()
      # now disk.id, etc. are available

    # without with statement
    disc = DiscId()
    disc.read()
    # now disk.id, etc. are available
    disc.free()

  This also requires the user to clean up the memory manually if the ``with``
  statement is not used. These details are hidden in `python-libdiscid`.
* Although `python-discid`'s :py:class:`discid.DiscId` properties are named similarly to the
  ones of the objects returned by :func:`libdiscid.read` and
  :func:`libdiscid.put`, there are a few properties which have different
  semantics in both libraries: :data:`libdiscid.DiscId.track_lengths` and
  :data:`libdiscid.DiscId.track_offsets` are noteworthy examples.

.. _GitHub: https://github.com/sebastinas/python-libdiscid
.. __: https://github.com/JonnyJD/python-discid
