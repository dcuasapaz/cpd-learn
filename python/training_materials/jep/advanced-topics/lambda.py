#!/usr/bin/python3
# Copyright 2019 Cloudera, Inc.
# Not to be reproduced or shared without prior written consent from Cloudera.

# These are the statements used in 
# Hands-On Exercise: Using Lambda Functions and Method Chaining

def do_something(the_function, the_value):
    return the_function(the_value)

driver_names = 'Logan,Brooke,James'

do_something(lambda x: x.split(','), driver_names)

driver_ratings = [4.5, 5, 3, 5, 3.5]

new_ratings = map(lambda x: x * 100, driver_ratings)

list(new_ratings)

non_perfect = filter(lambda x: int(x) != 500.0, new_ratings)

list(non_perfect)