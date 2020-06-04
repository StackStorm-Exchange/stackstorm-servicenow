# Licensed to the StackStorm, Inc ('StackStorm') under one or more
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

import mock
import yaml
import sys
sys.modules['pysnow'] = mock.Mock()

from st2tests.base import BaseActionTestCase
from get_non_structured import GetNonStructuredAction


class ServiceNowActionTestCase(BaseActionTestCase):

    action_cls = GetNonStructuredAction

    def setUp(self):
        super(ServiceNowActionTestCase, self).setUp()
        self._full_config = self.load_yaml('full.yaml')

    def load_yaml(self, filename):
        return yaml.safe_load(self.get_fixture_content(filename))

    @property
    def full_config(self):
        return self._full_config

    def test_get_instance_with_config(self):
        action = self.get_action_instance(self.full_config)

    def test_get_instance_without_config(self):
        # Use try/except as self.assertRaises wasn't matching
        try:
            self.get_action_instance(None)
            self.fail("Expection exception not thrown")
        except ValueError as e:
            self.assertTrue('Config for pack "tests" is missing' in e.args[0],
                            e.args)
