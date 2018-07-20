# -*- coding: utf-8 -*-
# Licensed to Anthony Shaw (anthonyshaw@apache.org) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .utils import scrub
from .models.provider import Provider


class ProvidersClient(object):
    """ Providers API. """

    def __init__(self, client):
        self.client = client

    def all(self, from_page=None):
        """
        Get all providers (will page results out)

        :param from_page: Start at page
        :type  from_page: ``int``

        :return: A list of providers
        :rtype: ``list`` of :class:`pathgather.models.provider.Provider`
        """
        params = {}

        if from_page is not None:
            params["from"] = from_page

        providers = self.client.get_paged("providers", params=params)
        results = []
        for page in providers:
            results.extend([self._to_provider(i) for i in page["results"]])
        return results

    def get(self, id):
        """
        Fetch a provider by ID.

        :param id: The provider id
        :type  id: ``str``

        :return: An instance :class:`pathgather.models.provider.Provider`
        :rtype: :class:`pathgather.models.provider.Provider`
        """
        provider = self.client.get("providers/{0}".format(id))
        return self._to_provider(provider)

    def create(
        self,
        name,
        custom_id=None,
        may_require_vpn=False,
        may_not_be_mobile_friendly=False,
    ):
        """
        Create a provider.

        :param name: The provider name
        :type  name: ``str``

        :param custom_id: Optional, but highly recommended
        :type  custom_id: ``str``

        :return: An instance :class:`pathgather.models.provider.Provider`
        :rtype: :class:`pathgather.models.provider.Provider`
        """
        params = {
            "name": name,
            "may_require_vpn": may_require_vpn,
            "may_not_be_mobile_friendly": may_not_be_mobile_friendly,
        }

        if custom_id:
            params["custom_id"] = custom_id

        provider = self.client.post("providers", {"provider": params})
        return self._to_provider(provider)

    def delete(self, id):
        """
        Delete a provider by ID.

        :param id: The provider ID
        :type  id: ``str``
        """
        self.client.delete("providers/{0}".format(id))

    def _to_provider(self, data):
        scrub(data)
        return Provider(**data)
