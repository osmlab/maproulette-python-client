.. maproulette-python-client documentation master file, created by
   sphinx-quickstart on Mon Mar 16 09:23:33 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

maproulette - a Python client for the MapRoulette API
=====================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage/getting_started
   usage/methods

---------------

This client makes it easy for users to communicate with the MapRoulette API from within
their Python environment.

**Sample Usage**:
   >>> import maproulette
   >>> config = maproulette.Configuration()
   >>> api = maproulette.Api(config)
   >>> api.get_project_by_id(4719)
   {'data': {'id': 4719, 'owner': 4785024, 'name': 'health_facilities_in_india',...}


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
