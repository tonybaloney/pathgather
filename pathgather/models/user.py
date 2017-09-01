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
class User(object):
    id = attrib()
    custom_id = attrib()
    custom_fields = attrib()
    first_name = attrib()
    last_name = attrib()
    created_at = attrib()
    updated_at = attrib()
    email = attrib()
    job_title = attrib()
    hire_date = attrib()
    location = attrib()
    deactivated = attrib()
    last_active_at = attrib()
    admin = attrib()
    department = attrib()
    user_skills = attrib()
