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

import json

from .models.content import Content, ContentProvider, UserContent, ContentComment
from .models.user import User
from .utils import scrub


class ContentClient(object):
    """ Content API. """

    def __init__(self, client):
        self.client = client

    def all(self, from_page=None, query=None, filter=None):
        """
        Get all content.

        :param from_page: Get from page
        :type  from_page: ``str``

        :param query: Additional filter query
            (see https://docs.pathgather.com/docs/filtering)
        :type  query: ``dict``

        :param filter: Additional type filter, e.g. "shared", "official", "pathgather"
        :type  filter: ``str``

        :return: A list of content
        :rtype: ``list`` of :class:`pathgather.models.content.Content`
        """
        params = {}

        if from_page is not None:
            params["from"] = from_page

        if not query and not filter:
            content = self.client.get_paged("content", params=params)
        else:
            extra = {}
            if query:
                extra["q"] = query
            if filter:
                extra["filter"] = filter
            data = json.dumps(extra)
            content = self.client.get_paged("content", params=params, data=data)

        results = []
        for page in content:
            results.extend([self._to_content(i) for i in page["results"]])
        return results

    def get(self, id):
        """
        Fetch a piece of content by ID.

        :param id: Returns an individual content item. The ID provided
         can be the ID assigned upon content creation,
         or a custom ID you assigned to the content.
        :type  id: ``str``

        :return: A piece of content
        :rtype: :class:`pathgather.models.content.Content`
        """
        user = self.client.get("content/{0}".format(id))
        return self._to_content(user)

    def create(
        self,
        name,
        content_type,
        source_url,
        topic_name,
        provider_name=None,
        provider_id=None,
        level=None,
        custom_id=None,
        description=None,
        image=None,
        tags=None,
        enabled=True,
        skills=None,
        duration=None,
    ):
        """
        Create a piece of content in the catalogue.

        :param name: Name/title of the content
        :type  name: ``str``

        :param content_type: The type of content being referenced
            Valid values are "Course", "Document", "Media", "Webinar", and "Webpage"
        :type  content_type: :class:`pathgather.types.ContentType` or ``str``

        :param source_url: The URL where this content can be found
        :type  source_url: ``str``

        :param topic_name: Specify the name of the topic via the topic_name field,
         or if you are using a custom_id, then please set the topic_custom_id field.
         Topic must already exist.
        :type  topic_name: ``str``

        :param provider_name: Specify the name of the provider via the
         provider_name field, or if you are using a custom_id, then please
         set the provider_id field. Provider must already exist
        :type  provider_name: ``str``

        :param provider_id: Specify the ID of the provider
        :type  provider_id: ``str``

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
        :rtype: :class:`pathgather.models.content.Content`
        """
        params = {
            "name": name,
            "content_type": content_type,
            "source_url": source_url,
            "topic_name": topic_name,
            "enabled": enabled,
        }
        if level:
            params["level"] = level
        if custom_id:
            params["custom_id"] = custom_id
        if description:
            params["description"] = description
        if image:
            params["image"] = image
        if tags:
            params["tags"] = tags
        if skills:
            params["skills"] = skills
        if duration:
            params["duration_str"] = duration
        if provider_name:
            params["provider_name"] = provider_name
        else:
            if provider_id:
                params["provider_custom_id"] = provider_id
            else:
                raise ValueError("provider_name or provider_id required")

        content = self.client.post("content", {"content": params})
        return self._to_content(content)

    def update(
        self,
        id,
        name=None,
        content_type=None,
        source_url=None,
        topic_name=None,
        provider_name=None,
        provider_id=None,
        level=None,
        custom_id=None,
        description=None,
        image=None,
        tags=None,
        enabled=True,
        skills=None,
        duration=None,
    ):
        """
        Update a piece of content.

        :param id: The content id
        :type  id: ``str``

        :param name: Name/title of the content
        :type  name: ``str``

        :param content_type: The type of content being referenced
            Valid values are "Course", "Document", "Media", "Webinar", and "Webpage"
        :type  content_type: :class:`pathgather.types.ContentType` or ``str``

        :param source_url: The URL where this content can be found
        :type  source_url: ``str``

        :param topic_name: Specify the name of the topic via the topic_name field,
         or if you are using a custom_id, then please set the topic_custom_id field.
         Topic must already exist.
        :type  topic_name: ``str``

        :param provider_name: Specify the name of the provider via the
         provider_name field, or if you are using a custom_id, then please
         set the provider_id field. Provider must already exist
        :type  provider_name: ``str``

        :param provider_id: Specify the ID of the provider
        :type  provider_id: ``str``

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
        :rtype: :class:`pathgather.models.content.Content`
        """
        params = {}
        if name:
            params["name"] = name
        if content_type:
            params["content_type"] = content_type
        if source_url:
            params["source_url"] = source_url
        if topic_name:
            params["topic_name"] = topic_name
        if enabled:
            params["enabled"] = enabled
        if level:
            params["level"] = level
        if custom_id:
            params["custom_id"] = custom_id
        if description:
            params["description"] = description
        if image:
            params["image"] = image
        if tags:
            params["tags"] = tags
        if skills:
            params["skills"] = skills
        if duration:
            params["duration_str"] = duration
        if provider_name:
            params["provider_name"] = provider_name
        if provider_id:
            params["provider_custom_id"] = provider_id

        content = self.client.put("content/{0}".format(id), {"content": params})
        return self._to_content(content)

    def delete(self, id):
        """
        Delete a piece of content

        :param id: The identifier
        :type  id: ``str``
        """
        self.client.delete("content/{0}".format(id))

    def starts_and_completions(self, from_page=None, query=None):
        """
        Returns objects representing a user's interaction
        (starts and completions) with content.
        User content items are returned sorted by start date,
        with the most recently started content appearing first.

        :param from_page: Get from page
        :type  from_page: ``str``

        :return: A list of content starts and completions
        :rtype: ``list`` of :class:`pathgather.models.content.UserContent`
        """
        params = {}

        if from_page is not None:
            params["from"] = from_page
        data = None
        if query:
            data = json.dumps({'q': query})
        content = self.client.get_paged("user_content", params=params, data=data)
        results = []
        for page in content:
            results.extend([self._to_user_content(i) for i in page["results"]])
        return results

    def log_completion(
        self, content_id, completed_at="now", user_id=None, user_email=None
    ):
        """
        Logs that a user completed content. Use this API to automatically update a user's
        Pathgather profile with learning activity that occurs in a different system.

        :param content_id: Can be the ID assigned upon creation, or a custom ID
        :type  content_id: ``str``

        :param completed_at: The time the content was completed by the user.
            Must be a parseable timestamp or the word 'now'
        :type  completed_at: ``str``

        :param user_id: Required unless you specify user_email.
            Can be the ID assigned upon creation, or a custom ID
        :type  user_id: ``str``

        :param user_email: Required unless you specify user_id.
            The email of the user that completed the content
        :type  user_email: ``str``

        :return: A registration of user content completion
        :rtype: :class:`pathgather.models.content.UserContent`
        """
        params = {"content_id": content_id, "completed_at": completed_at}
        if user_id:
            params["user_id"] = user_id
        else:
            if user_email:
                params["user_email"] = user_email
            else:
                raise ValueError("user_email or user_id required")

        content = self.client.post("user_content", params)
        return self._to_user_content(content)

    def get_comments(self, id, from_page=None, query=None):
        """
        Get comments on a content item
    
        :param id: The content item ID
        :type  id: ``str``

        :param from_page: Get from page
        :type  from_page: ``str``

        :param query: Extra query parameters
        :param query: ``dict``

        :return: A list of content item comments
        :rtype: ``list`` of :class:`pathgather.models.content.ContentComment`
        """
        params = {}

        if from_page is not None:
            params["from"] = from_page

        data = None
        if query is not None:
            data = json.dumps({"q": query})

        content = self.client.get_paged(
            "content/{0}/comments".format(id), params=params, data=data
        )
        results = []
        for page in content:
            results.extend([self._to_content_comment(i) for i in page["results"]])
        return results

    def create_comment(self, id, message, user_id, custom_id=None):
        """
        Create a comment on a content item

        :param id: The content item ID
        :type  id: ``str``

        :param message: The comment text, in plain or HTML
        :type  message: ``str``

        :param user_id: The ID of the user to create the comment as
        :type  user_id: ``str``

        :param custom_id: Custom identifier for the comment
        :type  custom_id: ``str``

        :return: A content item comment
        :rtype: :class:`pathgather.models.content.ContentComment`
        """
        params = {"message": message, "user_id": user_id}
        if custom_id:
            params["custom_id"] = custom_id

        response = self.client.post(
            "content/{0}/comments".format(id), {"comment": params}
        )
        return self._to_content_comment(response)

    def delete_comment(self, id, comment_id):
        """
        Delete a comment on a content item
 
        :param id: The content item ID
        :type  id: ``str``

        :param comment_id: The comment ID
        :type  comment_id: ``str``

        """
        return self.client.delete("content/{0}/comments/{1}".format(id, comment_id))

    def _to_content_comment(self, data):
        scrub(data)
        data["user"] = User(**data["user"])
        if "content" in data:
            data["content"] = Content(**data["content"])
        return ContentComment(**data)

    def _to_content(self, data):
        scrub(data)
        if "provider" in data:
            data["provider"] = ContentProvider(**data["provider"])
        return Content(**data)

    def _to_user_content(self, data):
        scrub(data)
        data["user"] = User(**data["user"])
        data["content"] = Content(**data["content"])
        data["content"].provider = ContentProvider(**data["content"].provider)
        return UserContent(**data)
