===============================
PathGather
===============================

.. image:: https://img.shields.io/pypi/v/pathgather.svg
        :target: https://pypi.python.org/pypi/pathgather

.. image:: https://img.shields.io/travis/tonybaloney/pathgather.svg
        :target: https://travis-ci.org/tonybaloney/pathgather

.. image:: https://readthedocs.org/projects/pathgather/badge/?version=latest
        :target: http://pathgather.readthedocs.io/en/latest/
        :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/tonybaloney/pathgather/badge.svg?branch=master
        :target: https://coveralls.io/github/tonybaloney/pathgather?branch=master
        :alt: Coverage Status


The Pathgather python package is for connecting to and leveraging the Pathgather REST API from Python 2 or 3.

This project is not part of Pathgather or operated by Pathgather, it is an open-source package for consuming their API.

* Free software: Apache 2 license
* Documentation: https://pathgather.readthedocs.org.

Example
-------

.. code-block:: python

        from pathgather import PathgatherClient
        import yaml
        import json
        from pprint import pprint

        with open('.tenant.yml', 'r') as tenant_yml:
           config = yaml.load(tenant_yml)

        client = PathgatherClient(config['host'], config['api_key'])

        print(client.users.all())

        with open('dump.json', 'r') as dump_j:
            data = json.load(dump_j)

        for user in data['users']:
            print('Creating {0}'.format(user['full_name']))
            new_user = client.users.create(
                name=user['full_name'], 
                job_title=user['job_title'],
                department='Learning and Development',
                email=user['email'])
            print(new_user)

        pprint(client.users.all())

        pprint(client.users.skills('362add1b-0a28-425b-a83c-40a6808fd094'))

        pprint(client.paths.all())

Features
--------

* User management
* Content management
* Path queries

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
