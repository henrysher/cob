# Cob: yet another yum S3 plugin
#
# Copyright 2014, Henry Huang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


install:
	install -m 0644 cob.conf /etc/yum/pluginconf.d/cob.conf
	install -m 0644 cob.py   /usr/lib/yum-plugins/cob.py
    
.PHONY: install
