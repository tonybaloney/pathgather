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
from .models.user import User
from .models.skill import Skill
from .models.gathering import (
    Gathering,
    GatheringUser,
    GatheringContent,
    GatheringInvite,
    GatheringPath,
)
from .models.content import Content
from .models.path import Path


class GatheringsClient(object):
    """ Gatherings API. """

    def __init__(self, client):
        self.client = client

    def all(self, from_page=None):
        """
        Get all gatherings (will page results out)

        :param from_page: Start at page
        :type  from_page: ``int``

        :return: A list of users
        :rtype: ``list`` of :class:`pathgather.models.gathering.Gathering`
        """
        params = {}

        if from_page is not None:
            params["from"] = from_page

        users = self.client.get_paged("gatherings", params=params)
        results = []
        for page in users:
            results.extend([self._to_gathering(i) for i in page["results"]])
        return results

    def get(self, id):
        """
        Fetch a gathering by ID.

        :param id: The gathering id
        :type  id: ``str``

        :return: An instance :class:`pathgather.models.gathering.Gathering`
        :rtype: :class:`pathgather.models.gathering.Gathering`
        """
        user = self.client.get("gatherings/{0}".format(id))
        return self._to_gathering(user)

    def create(
        self,
        name,
        custom_id=None,
        description=None,
        closed=True,
        image=None,
        skills=None,
    ):
        """
        Create a gathering.

        :param name: Name/title of the gathering
        :type  name: ``str``

        :param custom_id: Optional, but highly recommended if creating content via the API
        :type  custom_id: ``str``

        :param description: A description of the content to display to users
         when viewing it. Optional, but highly recommended
        :type  description: ``str``

        :param image: The URL to an image to display to users when viewing the content
        :type  image: ``str``

        :param closed: A flag representing whether this gathering is discoverable
         in your Pathgather catalog. If false,
         it will not show up in normal searches.
        :type  closed: ``bool``

        :param skills: An array of skills to associate to the content.
         Skills differ from tags, as they are displayed to the user and
         communicate the specific skill(s) the content will address.
        :type  skills: ``list`` of ``str``

        :return: A gathering
        :rtype: :class:`pathgather.models.gathering.Gathering`
        """
        params = {"name": name, "closed": closed}
        if custom_id:
            params["custom_id"] = custom_id
        if description:
            params["description"] = description
        if image:
            params["image"] = image
        if skills:
            params["skills"] = skills

        content = self.client.post("gatherings", {"gathering": params})
        return self._to_gathering(content)

    def update(
        self,
        id,
        name,
        custom_id=None,
        description=None,
        closed=True,
        image=None,
        skills=None,
    ):
        """
        Update a gathering.

        :param id: The gathering ID
        :type  id: ``str``

        :param name: Name/title of the gathering
        :type  name: ``str``

        :param custom_id: Optional, but highly recommended if creating content via the API
        :type  custom_id: ``str``

        :param description: A description of the content to display to users
         when viewing it. Optional, but highly recommended
        :type  description: ``str``

        :param image: The URL to an image to display to users when viewing the content
        :type  image: ``str``

        :param closed: A flag representing whether this gathering is discoverable
         in your Pathgather catalog. If false,
         it will not show up in normal searches.
        :type  closed: ``bool``

        :param skills: An array of skills to associate to the content.
         Skills differ from tags, as they are displayed to the user and
         communicate the specific skill(s) the content will address.
        :type  skills: ``list`` of ``str``

        :return: A gathering
        :rtype: :class:`pathgather.models.gathering.Gathering`
        """
        params = {}
        if name:
            params["name"] = name
        if closed:
            params["closed"] = closed
        if custom_id:
            params["custom_id"] = custom_id
        if description:
            params["description"] = description
        if image:
            params["image"] = image
        if skills:
            params["skills"] = skills

        content = self.client.put("gatherings/{0}".format(id), {"gathering": params})
        return self._to_gathering(content)

    def users(self, id, from_page=None):
        """
        Fetch a gathering's membership by ID.

        :param id: The gathering id
        :type  id: ``str``

        :return: An list of :class:`pathgather.models.gathering.UserGathering`
        :rtype: ``list`` of :class:`pathgather.models.gathering.UserGathering`
        """
        params = {}

        if from_page is not None:
            params["from"] = from_page

        users = self.client.get_paged("gatherings/{0}/users".format(id), params=params)
        results = []
        for page in users:
            results.extend([self._to_user_gathering(i) for i in page["results"]])
        return results

    def invite_user(self, id, user_id):
        """
        Invite a user to a gathering

        :param id: The gathering id
        :type  id: ``str``

        :param user_id: The user id
        :type  user_id: ``str``

        :return: An instance :class:`pathgather.models.gathering.UserGathering`
        :rtype: :class:`pathgather.models.gathering.UserGathering`
        """
        params = {"gathering_invite": {"invitee_id": user_id}}
        data = self.client.post("gatherings/{0}/gathering_invites".format(id), params)
        scrub(data)
        if "inviter" in data:
            data["inviter"] = User(**data["inviter"])
        if "invitee" in data:
            data["invitee"] = User(**data["invitee"])
        return GatheringInvite(**data)

    def remove_user(self, id, user_id):
        """
        Remove a user from a gathering

        :param id: The gathering id
        :type  id: ``str``

        :param user_id: The user id
        :type  user_id: ``str``
        """
        self.client.delete("gatherings/{0}/users/{1}".format(id, user_id))

    def content(self, id, from_page=None):
        """
        Fetch a gathering's content by ID.

        :param id: The gathering id
        :type  id: ``str``

        :return: An list of :class:`pathgather.models.gathering.GatheringUser`
        :rtype: ``list`` of :class:`pathgather.models.gathering.GatheringUser`
        """
        params = {}

        if from_page is not None:
            params["from"] = from_page

        content = self.client.get_paged(
            "gatherings/{0}/contents".format(id), params=params
        )
        results = []
        for page in content:
            results.extend([self._to_content_gathering(i) for i in page["results"]])
        return results

    def add_content(self, id, content_id):
        """
        Add a piece of content to a gathering

        :param id: The gathering id
        :type  id: ``str``

        :param content_id: The content id
        :type  content_id: ``str``

        :return: A dict
        :rtype: ``dict``
        """
        params = {
            "content": {
                "id": content_id
            }
        }
        content = self.client.post("gatherings/{0}/contents".format(id), params)
        return content

    def remove_content(self, id, content_id):
        """
        Remove content from a gathering

        :param id: The gathering id
        :type  id: ``str``

        :param content_id: The content id
        :type  content_id: ``str``
        """
        self.client.delete("gatherings/{0}/contents/{1}".format(id, content_id))

    def paths(self, id, from_page=None):
        """
        Fetch a gathering's paths by ID.

        :param id: The gathering id
        :type  id: ``str``

        :return: An list of :class:`pathgather.models.gathering.GatheringPath`
        :rtype: ``list`` of :class:`pathgather.models.gathering.GatheringPath`
        """
        params = {}

        if from_page is not None:
            params["from"] = from_page

        content = self.client.get_paged(
            "gatherings/{0}/paths".format(id), params=params
        )
        results = []
        for page in content:
            results.extend([self._to_path_gathering(i) for i in page["results"]])
        return results

    def remove_path(self, id, path_id):
        """
        Remove path from a gathering

        :param id: The gathering id
        :type  id: ``str``

        :param path_id: The path id
        :type  path_id: ``str``
        """
        self.client.delete("gatherings/{0}/paths/{1}".format(id, path_id))

    def delete(self, id):
        """
        Delete a gathering by ID.

        :param id: The gathering ID
        :type  id: ``str``
        """
        self.client.delete("gatherings/{0}".format(id))

    def _to_gathering(self, data):
        scrub(data)
        if "user" in data:
            data["user"] = User(**data["user"])
        if "skills" in data:
            _skills = []
            for skill in data["skills"]:
                _skills.append(Skill(**skill))
            data["skills"] = _skills
        return Gathering(**data)

    def _to_user_gathering(self, data):
        scrub(data)
        if "user" in data:
            data["user"] = User(**data["user"])
        if "gathering" in data:
            data["gathering"] = Gathering(**data["gathering"])
        return GatheringUser(**data)

    def _to_content_gathering(self, data):
        scrub(data)
        if "course" in data:
            data["course"] = Content(**data["course"])
        if "user" in data:
            data["user"] = User(**data["user"])
        if data["course"].sharer is not None:
            data["course"].sharer = User(**data["course"].sharer)
        return GatheringContent(**data)

    def _to_path_gathering(self, data):
        scrub(data)
        if "path" in data:
            data["path"] = Path(**data["path"])
        if "user" in data:
            data["user"] = User(**data["user"])

        return GatheringPath(**data)
