#!/usr/bin/python3
# Copyright 2019 Cloudera, Inc.
# Not to be reproduced or shared without prior written consent from Cloudera.


import sys
import processlog as pl


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

    try:
        # Open file and get the n-th line
        with open(file_location, 'r') as log_file:
            lines = log_file.readlines()
    except FileNotFoundError:
        print('Please provide the path to the log file')
        quit()

    process_log = pl.ProcessLog()

    record = lines[which_record]
    values = process_log.get_state_temp(record)
    process_log.display_state_temp(values[0], values[1], values[2])


