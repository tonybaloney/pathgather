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


class ContentClient(object):
    """ Content API. """

    def __init__(self, client):
        self.client = client

    def all(self, from_page=None):
        """
        Get all content.

        :param from_page: Filter by first name
        :type  from_page: ``int``

        :return: A list of content
        :rtype: ``list`` of ``dict``
        """
        params = {}

        if from_page is not None:
            params['from'] = from_page

        content = self.client.get_paged('content', params=params)
        results = []
        for page in content:
            results.extend([self._to_content(i) for i in page['results']])
        return results

    def get(self, id):
        """
        Fetch a piece of content by ID.

        :param id: Returns an individual content item. The ID provided
         can be the ID assigned upon content creation,
         or a custom ID you assigned to the content.
        :type  id: ``str``

        :return: A piece of content
        :rtype: ``dict``
        """
        user = self.client.get('content/{0}'.format(id))
        return self._to_content(user)

    def create(self, name, content_type, source_url,
               provider_name, topic_name, level=None, custom_id=None,
               description=None, image=None, tags=None, enabled=True,
               skills=None, duration=None):
        """
        Create a piece of content in the catalogue.

        :param name: Name/title of the content
        :type  name: ``str``

        :param content_type: The type of content being referenced
            Valid values are "Course", "Document", "Media", "Webinar", and "Webpage"
        :type  content_type: :class:`pathgather.types.ContentType` or ``str``

        :param source_url: The URL where this content can be found
        :type  source_url: ``str``

        :param provider_name: Specify the name of the provider via the
        provider_name field, or if you are using a custom_id, then please
         set the provider_custom_id field. Provider must already exist
        :type  provider_name: ``str``

        :param topic_name: Specify the name of the topic via the topic_name field,
         or if you are using a custom_id, then please set the topic_custom_id field.
         Topic must already exist.
        :type  topic_name: ``str``

        :param level: The difficulty/experience level of the content
        Valid values are "Beginner", "Intermediate", "Advanced", "Expert", and "All"
        :type  level: :class:`pathgather.types.SkillLevel` or ``str``

        :param custom_id: Optional, but highly recommended if creating content via the API
        :type  custom_id: ``str``

        :param description: A description of the content to display to users
         when viewing it. Optional, but highly recommended
        :type  description: ``str``

        :param image: The URL to an image to display to users when viewing the content
        :type  image: ``str``

        :param tags: An array of tags to associate to the content.
         Tags are primarily used for easy lookup later.
        :type  tags: ``list`` of ``str``

        :param enabled: A flag representing whether this content is discoverable
        in your Pathgather content catalog. If false,
        it will not show up in normal content searches.
        :type  enabled: ``bool``

        :param skills: An array of skills to associate to the content.
        Skills differ from tags, as they are displayed to the user and
        communicate the specific skill(s) the content will address.
        :type  skills: ``list`` of ``str``

        :param duration:Set to a value that represents the amount of time
         needed to complete the content.
         A wide variety of inputs are accepted ('3 mins 4 sec', '2 hrs 20 min', etc).
         An error will be returned if the format is unknown. Integer values are also
         accepted and are assumed to be in seconds.
        :type  duration: ``str``

        :return: A piece of content
        :rtype: ``dict``
        """
        params = {
            'name': name,
            'content_type': content_type,
            'source_url': source_url,
            'provider_name': provider_name,
            'topic_name': topic_name,
            'enabled': enabled
        }
        if level:
            params['level'] = level
        if custom_id:
            params['custom_id'] = custom_id
        if description:
            params['description'] = description
        if image:
            params['image'] = image
        if tags:
            params['tags'] = tags
        if skills:
            params['skills'] = skills
        if duration:
            params['duration_str'] = duration

        content = self.client.post('content', {'content': params})
        return self._to_content(content)

    def delete(self, id):
        """
        Delete a piece of content

        :param id: The identifier
        :type  id: ``str``
        """
        self.client.delete('content/{0}'.format(id))

    def _to_content(self, data):
        # TODO : Reflect into class model
        return data
