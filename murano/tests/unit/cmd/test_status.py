# Copyright (c) 2018 NEC, Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_upgradecheck.upgradecheck import Code

from murano.cmd import status
from murano.tests.unit import base


class TestUpgradeChecks(base.MuranoTestCase):

    def setUp(self):
        super(TestUpgradeChecks, self).setUp()
        self.cmd = status.Checks()

    def test__sample_check(self):
        check_result = self.cmd._sample_check()
        self.assertEqual(
            Code.SUCCESS, check_result.code)
