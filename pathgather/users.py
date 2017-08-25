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
    """ Users API. """

    def __init__(self, client):
        self.client = client

    def all(self, from_page=None):
        """
        Get all users.

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

    def get(self, id):
        """
        Fetch a user by ID.

        :param id: The identifier
        :type  id: ``str``

        :return: An instance :class:`User`
        :rtype: :class:`User`
        """
        user = self.client.get('users/{0}'.format(id))
        return self._to_user(user)

    def create(self, name, job_title, department,
               email, saml_id=None, custom_id=None, hire_date=None,
               location='', avatar='', admin=False, send_invite=True,
               deactivated=False, custom_fields=None):
        params = {
            'name': name,
            'job_title': job_title,
            'department': department,
            'email': email,
            'admin': admin,
            'send_invite': send_invite,
            'deactivated': deactivated
        }
        if saml_id:
            params['saml_id'] = saml_id
        if custom_id:
            params['custom_id'] = custom_id
        if hire_date:
            params['hire_date'] = hire_date
        if location:
            params['location'] = location
        if avatar:
            params['avatar'] = avatar
        if custom_fields:
            params['custom_fields'] = custom_fields

        user = self.client.post('users', {'user': params})
        return self._to_user(user)

    def _to_user(self, data):
        # TODO : Reflect into class model
        return data
