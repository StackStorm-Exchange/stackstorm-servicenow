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

from servicenow_base_action_test_case import ServiceNowBaseActionTestCase
from upload_attachment import UploadAttachmentAction


class UploadAttachmentActionTestCase(ServiceNowBaseActionTestCase):

    action_cls = UploadAttachmentAction

    def setUp(self):
        super(UploadAttachmentActionTestCase, self).setUp()

    @mock.patch('pysnow.Client')
    def test_add_attachment(self, mock_client):
        action = self.get_action_instance(self.full_config)
        result = action.run('table1','file1','sysid1')
        mock_client.return_value.query.assert_called_with(table="table1", query={'sys_id': "sysid1"})
        mock_client.return_value.query.return_value.attach.assert_called_with('file1')       
        self.assertIsNotNone(result)
        self.assertTrue(result[0])
