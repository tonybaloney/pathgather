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
class Gathering(object):
    id = attrib()
    name = attrib()
    created_at = attrib(default=None)
    custom_id = attrib(default=None)
    description = attrib(default=None)
    closed = attrib(default=False)
    users_count = attrib(default=0)
    courses_count = attrib(default=0)
    paths_count = attrib(default=0)
    image = attrib(default=None)
    conversations_count = attrib(default=0)
    updated_at = attrib(default=None)
    user = attrib(default=None)
    skills = attrib(default=None)


@attrs
class GatheringInvite(object):
    id = attrib()
    created_at = attrib(default=None)
    inviter = attrib(default=None)
    invitee = attrib(default=None)


@attrs
class GatheringUser(object):
    id = attrib()
    created_at = attrib()
    gathering = attrib()
    user = attrib()
    is_admin = attrib()
    auto_assigned = attrib()


@attrs
class GatheringContent(object):
    id = attrib()
    created_at = attrib()
    user = attrib()
    course = attrib()


@attrs
class GatheringPath(object):
    id = attrib()
    created_at = attrib()
    user = attrib()
    path = attrib()
    added_by_admin = attrib(default=False)
