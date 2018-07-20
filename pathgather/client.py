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

import requests

from pathgather.exceptions import PathgatherApiException
from .users import UsersClient
from .content import ContentClient
from .paths import PathsClient
from .gatherings import GatheringsClient
from .skills import SkillsClient
from .providers import ProvidersClient


class PathgatherClient(object):
    """
    The main API client
    """

    """
    Set the default results per page. Max 100
    """
    results_per_page = 50

    def __init__(self, host, api_key, proxy=None, skip_ssl_validation=False):
        """
        Instantiate a new API client

        :param host: The host name, e.g. mycompany.pathgather.com
        :type  host: ``str``

        :param api_key: The API token (from the admin console)
        :type  api_key: ``str``

        :param proxy: The proxy to connect through
        :type  proxy: ``str``

        :param skip_ssl_validation: Skip SSL validation
        :type  skip_ssl_validation: ``bool``
        """
        self._api_key = api_key

        self.base_url = "https://{0}/v1".format(host)

        self.session = requests.Session()
        if proxy:
            self.session.proxies = {"https": proxy}
        if skip_ssl_validation:
            self.session.verify = False
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(api_key),
            }
        )

        self._users = UsersClient(self)
        self._content = ContentClient(self)
        self._paths = PathsClient(self)
        self._gatherings = GatheringsClient(self)
        self._skills = SkillsClient(self)
        self._providers = ProvidersClient(self)

    def get(self, uri, params=None, data=None):
        try:
            if params:
                if "per_page" not in params:
                    params["per_page"] = self.results_per_page
            else:
                params = {"per_page": self.results_per_page}
            result = self.session.get(
                "{0}/{1}".format(self.base_url, uri), params=params, data=data
            )
            result.raise_for_status()

            return result.json()
        except requests.HTTPError as e:
            raise PathgatherApiException(e.response.text, uri)

    def get_paged(self, uri, params=None, data=None):
        try:
            page = None
            end = False
            while not end:
                result = self.get(uri, params={"from": page}, data=data)
                next_page = result["next"]
                yield result
                if next_page:
                    page = next_page
                else:
                    end = True
        except requests.HTTPError as e:
            raise PathgatherApiException(e.response.text, uri)

    def post(self, uri, data=None):
        try:
            result = self.session.post("{0}/{1}".format(self.base_url, uri), json=data)
            result.raise_for_status()

            return result.json()
        except requests.HTTPError as e:
            raise PathgatherApiException(e.response.text)

    def put(self, uri, data=None):
        try:
            result = self.session.put("{0}/{1}".format(self.base_url, uri), json=data)
            result.raise_for_status()
            if result.text:
                return result.json()
        except requests.HTTPError as e:
            raise PathgatherApiException(e.response.text)

    def delete(self, uri):
        try:
            result = self.session.delete("{0}/{1}".format(self.base_url, uri))
            result.raise_for_status()
        except requests.HTTPError as e:
            raise PathgatherApiException(e.response.text)

    @property
    def users(self):
        """
        Users

        :rtype: :class:`pathgather.users.UserClient`
        """
        return self._users

    @property
    def content(self):
        """
        Learning Content

        :rtype: :class:`pathgather.content.ContentClient`
        """
        return self._content

    @property
    def paths(self):
        """
        Learning Paths

        :rtype: :class:`pathgather.paths.PathsClient`
        """
        return self._paths

    @property
    def gatherings(self):
        """
        Learner Gatherings

        :rtype: :class:`pathgather.gatherings.GatheringsClient`
        """
        return self._gatherings

    @property
    def skills(self):
        """
        Pathgather Skills

        :rtype: :class:`pathgather.skills.SkillsClient`
        """
        return self._skills

    @property
    def providers(self):
        """
        Pathgather Providers

        :rtype: :class:`pathgather.providers.ProvidersClient`
        """
        return self._providers
