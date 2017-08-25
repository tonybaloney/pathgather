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


class UsersClient(object):
    """
    Users API
    """
    def __init__(self, client):
        self.client = client

    def get_all_users(self, from_page=None):
        """
        Get all users

        :param from_page: Filter by first name
        :type  from_page: ``int``

        :return: A list of :class:`User`
        :rtype: ``list`` of :class:`User`
        """
        params = {}

        if from_page is not None:
            params['from'] = from_page

        users = self.client.get('users', params=params)
        return [self._to_user(i) for i in users['results']]

    def get_user(self, id):
        """
        Fetch a user by ID

        :param id: The identifier
        :type  id: ``str``

        :return: An instance :class:`User`
        :rtype: :class:`User`
        """
        user = self.client.get('users/{0}'.format(id))
        return self._to_user(user)

    def _to_user(self, data):
        # TODO : Reflect into class model
        return data
