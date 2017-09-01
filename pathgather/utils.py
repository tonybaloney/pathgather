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


def scrub(obj, bad="_type"):
    """
    Scrub the _type dict item recursively

    Credit https://stackoverflow.com/a/20692955/7402337
    """
    if isinstance(obj, dict):
        for k in list(obj.keys()):
            if k == bad:
                del obj[k]
            else:
                scrub(obj[k], bad)
    elif isinstance(obj, list):
        for i in reversed(range(len(obj))):
            if obj[i] == bad:
                del obj[i]
            else:
                scrub(obj[i], bad)

    else:
        # neither a dict nor a list, do nothing
        pass
