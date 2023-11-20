#!/usr/bin/python3
# Copyright 2019 Cloudera, Inc.
# Not to be reproduced or shared without prior written consent from Cloudera.

# These are the statements used in 
# Hands-On Exercise: Working with Files


driver_file = open('drivers.txt', 'w+')

driver_file.write('Logan\n')
driver_file.write('Brooke\n')
driver_file.write('Jack\n')
driver_file.write('James\n')

driver_file.close()

with open('drivers.txt', 'r') as driver_file:
    all_lines = driver_file.readlines()

all_lines