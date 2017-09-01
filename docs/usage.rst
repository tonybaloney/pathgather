=====
Usage
=====

To use PathGather in a project::

.. code-block:: python

    from pathgather import PathgatherClient
    import yaml
    from pprint import pprint

    with open('.tenant.yml', 'r') as tenant_yml:
        config = yaml.load(tenant_yml)

    client = PathgatherClient(config['host'], config['api_key'])


Proxy Settings
--------------

The client object can be given a HTTP proxy and optionally SSL validation can be disabled.
This is useful for Fiddler/Charles type debugging proxies.

.. code-block:: python

    from pathgather import PathgatherClient
    import yaml
    from pprint import pprint

    with open('.tenant.yml', 'r') as tenant_yml:
        config = yaml.load(tenant_yml)

    client = PathgatherClient(config['host'], config['api_key'], proxy='http://localhost:8888/', skip_ssl_validation=True)

    pprint(client.users.all())

User Management
---------------

Getting a list of users
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from pathgather import PathgatherClient
    from pprint import pprint
    client = PathgatherClient(...)

    pprint(client.users.all())
