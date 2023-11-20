#!/usr/bin/python3
# Copyright 2019 Cloudera, Inc.
# Not to be reproduced or shared without prior written consent from Cloudera.


class ProcessLog():
    """This class is used to process a log"""

    def __init__(self):
        print('Class created')

    def get_state_temp(self, one_record):
        """This function retrieves the state of radios and temp from one record"""
        entries = one_record.split(',')
        bluetooth = entries[6]
        wifi = entries[7]
        dev_temp = int(entries[5])
        return (bluetooth, wifi, dev_temp)


    def display_state_temp(self, bluetooth, wifi, dev_temp):
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
    print('Please import this class')
