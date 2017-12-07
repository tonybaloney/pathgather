Example solutions
-----------------


Saving Tenant API details
=========================

In these examples, create the files `.tenant.prod.yml` and `.tenant.dev.yml` for production and development environments.

.. code-block:: yaml

    pathgather_token = '<api token>'
    pathgather_host = 'mycompany.pathgather.com'

Reading an RSS feed for a podcast and loading episodes
======================================================

This example assumes that :
 * For each feed URL you have created a Provider with the custom_id matching the Podcast name in the tuple
 * You want to tag skills for each episodes
 * You create a tenant configuration with the API key.

.. literalinclude:: /examples/podcast.py
   :language: python

This will load Podcast episodes with the description, links, tags and skills.

.. figure:: /_static/images/podcast.jpeg
    :align: center


Scraping a JSON file on a website and linking learning content
==============================================================

This is essentially a custom provider implementation, targeting Cisco Learning Labs. 

.. literalinclude:: /examples/scrape.py
   :language: python