#!/usr/bin/python3
# Copyright 2019 Cloudera, Inc.
# Not to be reproduced or shared without prior written consent from Cloudera.

# These are the statements used in 
# Hands-On Exercise: Using Lambda Functions and Method Chaining

pd.read_csv('rides.txt').to_parquet('rides_two.parquet')