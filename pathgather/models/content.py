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
class Content(object):
    id = attrib()
    name = attrib()
    content_type = attrib()
    source_url = attrib()
    created_at = attrib()
    enabled = attrib()
    skills = attrib(default=None)
    tags = attrib(default=None)
    rating = attrib(default=0)
    reviews_count = attrib(default=0)
    level = attrib(default=None)
    duration = attrib(default=None)
    updated_at = attrib(default=None)
    provider = attrib(default=None)
    topic = attrib(default=None)
    custom_id = attrib(default=None)


@attrs
class ContentProvider(object):
    id = attrib()
    created_at = attrib()
    name = attrib()
    custom_id = attrib(default=None)
