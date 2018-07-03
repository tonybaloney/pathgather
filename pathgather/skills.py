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
from .models.skill import Skill


class SkillsClient(object):
    """ Skills API. """

    def __init__(self, client):
        self.client = client

    def all(self, from_page=None):
        """
        Get all skills (will page results out)

        :param from_page: Start at page
        :type  from_page: ``int``

        :return: A list of users
        :rtype: ``list`` of :class:`pathgather.models.skill.Skill`
        """
        params = {}

        if from_page is not None:
            params["from"] = from_page

        users = self.client.get_paged("skills", params=params)
        results = []
        for page in users:
            results.extend([self._to_skill(i) for i in page["results"]])
        return results

    def get(self, id):
        """
        Fetch a skill by ID.

        :param id: The user id
        :type  id: ``str``

        :return: An instance :class:`pathgather.models.skill.Skill`
        :rtype: :class:`pathgather.models.skill.Skill`
        """
        user = self.client.get("skills/{0}".format(id))
        return self._to_skill(user)

    def create(self, name, custom_id=None):
        """
        Create a skill.

        :param name: The skill name
        :type  name: ``str``

        :param custom_id: Optional, but highly recommended
        :type  custom_id: ``str``

        :return: An instance :class:`pathgather.models.skill.Skill`
        :rtype: :class:`pathgather.models.skill.Skill`
        """
        params = {"name": name}

        if custom_id:
            params["custom_id"] = custom_id

        user = self.client.post("skills", {"skill": params})
        return self._to_skill(user)

    def update(self, id, name=None, custom_id=None):
        """
        Update a skill.

        :param id: The skill id
        :type  id: ``str``

        :param name: The skill name
        :type  name: ``str``

        :param custom_id: Optional, but highly recommended
        :type  custom_id: ``str``

        :return: An instance :class:`pathgather.models.skill.Skill`
        :rtype: :class:`pathgather.models.skill.Skill`
        """
        params = {}
        if name:
            params["name"] = name
        if custom_id:
            params["custom_id"] = custom_id

        user = self.client.put("skills/{0}".format(id), {"user": params})
        return self._to_skill(user)

    def delete(self, id):
        """
        Delete a skill by ID.

        :param id: The skill ID
        :type  id: ``str``
        """
        self.client.delete("skills/{0}".format(id))

    def _to_skill(self, data):
        scrub(data)
        return Skill(**data)
