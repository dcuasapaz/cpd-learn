#!/usr/bin/python3
# Copyright 2019 Cloudera, Inc.
# Not to be reproduced or shared without prior written consent from Cloudera.
import sys


def get_state_temp(one_record):
    """This function retrieves the state of radios and temp from one record"""
    entries = one_record.split(',')
    bluetooth = entries[6]
    wifi = entries[7]
    dev_temp = int(entries[5])
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
    """This program displays the state of radios and temp from a log file

    Parameters
    ----------
    file_location (argv[1]): which file to read
    which_record (argv[2]): the line that contains the record we want 
    """

    # Set the variables
    file_location = sys.argv[1]
    which_record = int(sys.argv[2])

    # Open file and get the n-th line
    with open(file_location, 'r') as log_file:
        lines = log_file.readlines()

    record = lines[which_record]
    values = get_state_temp(record)
    display_state_temp(values[0], values[1], values[2])


