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
        Get all users (will page results out)

        :param from_page: Start at page
        :type  from_page: ``int``

        :return: A list of users
        :rtype: ``list`` of ``dict``
        """
        params = {}

        if from_page is not None:
            params['from'] = from_page

        users = self.client.get_paged('users', params=params)
        results = []
        for page in users:
            results.extend([self._to_user(i) for i in page['results']])
        return results

    def get(self, id):
        """
        Fetch a user by ID.

        :param id: The user id
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
        """
        Create a user.

        :param name: The users' name
        :type  name: ``str``

        :param job_title: The users' job title
        :type  job_title: ``str``

        :param department: If the department specified here matches the same
         name as an existing department, the user will be added to the existing
         department. If the department is not found, it will be created
         and the user added to it.
        :type  department: ``str``

        :param email: The users' email address
        :type  email: ``str``

        :param saml_id: Required ONLY if your organization has SAML SSO enabled
        :type  saml_id: ``str``

        :param custom_id: Optional, but highly recommended
        :type  custom_id: ``str``

        :param hire_date: The hire date for the user
        :type  hire_date: ``str`` or ``datetime.date``

        :param location: Location of the user, e.g. Paris, France
        :type  location: ``str``

        :param avatar: The URL to an image of the user
        :type  avatar: ``str``

        :param admin: Is user an admin?
        :type  admin: ``bool``

        :param send_invite: Send invite after creation via email?
        :type  send_invite: ``bool``

        :param deactivated: Is user deactivated?
        :type  deactivated: ``bool``

        :param custom_fields: Any custom fields for this user
        :type  custom_fields: ``dict``

        :return: An instance :class:`User`
        :rtype: :class:`User`
        """
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

    def update(self, id, name=None, job_title=None, department=None,
               email=None, saml_id=None, custom_id=None, hire_date=None,
               location=None, avatar=None, admin=None,
               deactivated=None, custom_fields=None):
        """
        Update a user.

        :param id: The user id
        :type  id: ``str``

        :param name: The users' name
        :type  name: ``str``

        :param job_title: The users' job title
        :type  job_title: ``str``

        :param department: If the department specified here matches the same
         name as an existing department, the user will be added to the existing
         department. If the department is not found, it will be created
         and the user added to it.
        :type  department: ``str``

        :param email: The users' email address
        :type  email: ``str``

        :param saml_id: Required ONLY if your organization has SAML SSO enabled
        :type  saml_id: ``str``

        :param custom_id: Optional, but highly recommended
        :type  custom_id: ``str``

        :param hire_date: The hire date for the user
        :type  hire_date: ``str`` or ``datetime.date``

        :param location: Location of the user, e.g. Paris, France
        :type  location: ``str``

        :param avatar: The URL to an image of the user
        :type  avatar: ``str``

        :param admin: Is user an admin?
        :type  admin: ``bool``

        :param deactivated: Is user deactivated?
        :type  deactivated: ``bool``

        :param custom_fields: Any custom fields for this user
        :type  custom_fields: ``dict``

        :return: An instance :class:`User`
        :rtype: :class:`User`
        """
        params = {}
        if name:
            params['name'] = name
        if job_title:
            params['job_title'] = job_title
        if department:
            params['department'] = department
        if email:
            params['email'] = email
        if admin is not None:
            params['admin'] = admin
        if deactivated is not None:
            params['deactivated'] = deactivated
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

        user = self.client.put('users/{0}'.format(id), {'user': params})
        return self._to_user(user)

    def delete(self, id):
        """
        Delete a user by ID.

        :param id: The identifier
        :type  id: ``str``
        """
        self.client.delete('users/{0}'.format(id))

    def _to_user(self, data):
        # TODO : Reflect into class model
        return data
