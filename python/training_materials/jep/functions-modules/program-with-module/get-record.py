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

    # Open file and get the n-th line
    with open(file_location, 'r') as log_file:
        lines = log_file.readlines()

    record = lines[which_record]
    values = pl.get_state_temp(record)
    pl.display_state_temp(values[0], values[1], values[2])


