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
import attr
import arrow


@attrs
class Provider(object):
    id = attrib()
    name = attrib()

    may_require_vpn = attr.ib(converter=bool)
    may_not_be_mobile_friendly = attr.ib(converter=bool)
    is_subscribed = attr.ib(converter=bool)

    created_at = attr.ib(converter=attr.converters.optional(arrow.get))
    updated_at = attr.ib(converter=attr.converters.optional(arrow.get))

    custom_id = attrib(default=None)
