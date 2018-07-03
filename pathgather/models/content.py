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

import arrow
from attr import attrs, attrib
import attr


@attrs
class Content(object):
    id = attrib()
    name = attrib()
    content_type = attrib()
    source_url = attrib()
    enabled = attrib()

    created_at = attr.ib(converter=attr.converters.optional(arrow.get), default=None)
    description = attrib(default="")
    instructor = attrib(default=None)
    skills = attrib(default=None)
    tags = attrib(default=None)
    rating = attrib(default=0)
    reviews_count = attrib(default=0)
    level = attrib(default=None)
    duration = attrib(default=None)
    updated_at = attr.ib(converter=attr.converters.optional(arrow.get), default=None)
    provider = attrib(default=None)
    topic = attrib(default=None)
    custom_id = attrib(default=None)
    start_date = attr.ib(converter=attr.converters.optional(arrow.get), default=None)
    end_date = attr.ib(converter=attr.converters.optional(arrow.get), default=None)
    deactivated = attrib(default=False)
    sharer_id = attrib(default=None)
    publicly_accessible = attrib(default=True)
    endorsement_count = attrib(default=0)
    sharer = attrib(default=None)


@attrs
class ContentProvider(object):
    id = attrib()
    name = attrib()

    created_at = attr.ib(converter=attr.converters.optional(arrow.get), default=None)
    updated_at = attr.ib(converter=attr.converters.optional(arrow.get), default=None)
    may_require_vpn = attrib(default=False)
    may_not_be_mobile_friendly = attrib(default=False)
    is_subscribed = attrib(default=True)
    custom_id = attrib(default=None)


@attrs
class UserContent(object):
    id = attrib()
    public = attrib(default=False)
    started_at = attr.ib(converter=attr.converters.optional(arrow.get), default=None)
    completed_at = attr.ib(converter=attr.converters.optional(arrow.get), default=None)
    user = attrib(default=None)
    content = attrib(default=None)
    created_at = attr.ib(converter=attr.converters.optional(arrow.get), default=None)
    updated_at = attr.ib(converter=attr.converters.optional(arrow.get), default=None)
    first_launched_at = attr.ib(
        converter=attr.converters.optional(arrow.get), default=None
    )
    last_launched_at = attr.ib(
        converter=attr.converters.optional(arrow.get), default=None
    )
    saved_at = attr.ib(converter=attr.converters.optional(arrow.get), default=None)


@attr.s
class ContentComment(object):
    id = attrib()
    created_at = attr.ib(converter=attr.converters.optional(arrow.get), default=None)
    updated_at = attr.ib(converter=attr.converters.optional(arrow.get), default=None)
    message = attr.ib(default=None)
    content = attr.ib(default=None)
    conversation = attr.ib(default=None)
    path = attr.ib(default=None)
    custom_id = attr.ib(default=None)
    user = attr.ib(default=None)
