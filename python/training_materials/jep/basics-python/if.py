#!/usr/bin/python3
# Copyright 2019 Cloudera, Inc.
# Not to be reproduced or shared without prior written consent from Cloudera.

# These are the statements used in 
# Hands-On Exercise: Controlling Program Flow

# Experiment with different values
temp = 105

if temp <= 50:
    print('Shiver')
elif temp > 100:
    print('Sweat')
elif temp > 120:
    print('Be careful')
else:
    print('Smile')