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

from attr import attrs, attrib


@attrs
class Path(object):
    id = attrib()
    name = attrib()
    created_at = attrib()
    published = attrib()
    description = attrib(default=None)
    url = attrib(default=None)
    user_id = attrib(default=None)
    slug = attrib(default=None)
    user_started_count = attrib(default=0)
    user_completed_count = attrib(default=0)
    privately_started_count = attrib(default=0)
    privately_completed_count = attrib(default=0)
    privately_started_count = attrib(default=0)
    courses_count = attrib(default=0)
    comments_count = attrib(default=0)
    created_at_unix = attrib(default=None)
    topic_id = attrib(default=None)
    image = attrib(default=None)
    endorsed = attrib(default=False)
    promoted = attrib(default=None)
    added_by_admin = attrib(default=False)
    path_sections_count = attrib(default=0)
    endorsed_count = attrib(default=0)
    publicly_accessible = attrib(default=None)
    updated_at = attrib(default=None)
    saved_at = attrib(default=None)
    published_at = attrib(default=None)
    custom_id = attrib(default=None)
    tags = attrib(default=None)
    skills = attrib(default=None)
    user = attrib(default=None)
    gatherings = attrib(default=None)
    endorsement_count = attrib(default=0)


@attrs
class UserPath(object):
    id = attrib()
    public = attrib(default=False)
    started_at = attrib(default=None)
    created_at = attrib(default=None)
    saved_at = attrib(default=None)
    completed_at = attrib(default=None)
    user = attrib(default=None)
    path = attrib(default=None)
    updated_at = attrib(default=None)
    percentage = attrib(default=0)
