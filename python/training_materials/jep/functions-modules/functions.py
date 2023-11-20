#!/usr/bin/python3
# Copyright 2019 Cloudera, Inc.
# Not to be reproduced or shared without prior written consent from Cloudera.

# These are the statements used in 
# Hands-On Exercise: Creating Functions and Modules

def add_them(operand_one, operand_two):
    print('Adding two values')
    result = operand_one + operand_two
    return result

added = add_them(40, 2)

add_function = add_them

add_function(40, 2)

def add_op(operand_one, operand_two): return operand_one + operand_two

add_op(40, 2)
