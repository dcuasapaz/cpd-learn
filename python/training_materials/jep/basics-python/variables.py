#!/usr/bin/python3
# Copyright 2019 Cloudera, Inc.
# Not to be reproduced or shared without prior written consent from Cloudera.

# These are the statements used in 
# Hands-On Exercise: Working with Variables 

the_answer

the_answer = 42

the_answer = 42 # Write only the_a and hit tab in IPython for autocomplete

type(the_answer)

the_answer = 'Forty two'

the_answer?

the_answer=42.0
the_answer=[40, 2]
the_answer=(40, 2)
the_answer={'answer', 42}
the_answer={'answer': 42}

another_answer = the_answer = 16

another_answer, the_answer = 'Forty two', 42 

str(the_answer)

new_answer = another_answer + ":" + str(the_answer)

float(42)

int(3.14159)

hex(64)

type(hex(64)