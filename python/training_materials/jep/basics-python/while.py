#!/usr/bin/python3
# Copyright 2019 Cloudera, Inc.
# Not to be reproduced or shared without prior written consent from Cloudera.

# These are the statements used in 
# Hands-On Exercise: Controlling Program Flow


driver_accidents = 0
while driver_accidents < 5:
    driver_accidents = driver_accidents + 1
    print('Accidents ' + str(driver_accidents))

driver_accidents = 0
while driver_accidents < 5:
    driver_accidents = driver_accidents + 1
    if driver_accidents == 3:
        break
    print('Accidents ' + str(driver_accidents))

driver_accidents = 0
while driver_accidents < 5:
    driver_accidents = driver_accidents + 1
    if driver_accidents == 3:
        continue
    print('Accidents ' + str(driver_accidents))