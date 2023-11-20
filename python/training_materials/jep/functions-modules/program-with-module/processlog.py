#!/usr/bin/python3
# Copyright 2018 Cloudera, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def get_state_temp(one_record):
    """This function retrieves the state of radios and temp from one record"""
    bluetooth = one_record[92:99]
    wifi = one_record[100:107]
    dev_temp = int(one_record[58:60])
    return (bluetooth, wifi, dev_temp)


def display_state_temp(bluetooth, wifi, dev_temp):
    # Determine state of radios
    print('Bluetooth is ON :', bluetooth == 'enabled')
    print('Wifi is ON      :', wifi == 'enabled')
    print('Wifi is ONLINE  :', wifi == 'connected')
    # Determine whether the device temperature is above 50 degrees
    if dev_temp > 50:
        print('Device temp is more than 50 degrees')
    else:
        print('Device temp is normal')


if __name__ == "__main__":
    print('Process log initialized')