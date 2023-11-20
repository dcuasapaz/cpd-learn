#!/usr/bin/python3
# Copyright 2019 Cloudera, Inc.
# Not to be reproduced or shared without prior written consent from Cloudera.

# These are the statements used in 
# Hands-On Exercise: Essential & Data Science Libraries

# Python Standard Library
import platform

platform.python_version()

import collections

driver_collection = collections.Counter(['Logan', 'Brooke', 'James', 'Jack', 'James', 'Brooke', 'James'])

driver_collection.most_common(2)


# Numpy
driver_score = [4, 4.5, 3.5, 4, 2]

import numpy as np

np.mean(driver_score)

driver_nda = np.array(driver_score)

driver_nda.mean()

driver_nda.dtype

driver_nda * 100

driver_nda.shape

driver_nda.size

drivers_ratings = [[4,4.5,3.5], [3.5,4,3], [5,5,4.5], [5,5,4.5]]

np.array(driver_ratings)


# Using pandas, the Data Analysis Library
devices_csv = pd.read_csv('devices.csv')

devices_csv.head()

devices_csv = pd.read_csv('devices.csv', delimiter='\t')

devices_csv[:5][make]

devices_mm = devices_csv[['make', 'model']]

devices_csv.groupby('make').size()

devices_csv.to_json('devices.json', orient='records', lines=True) 

# Using matplotlib to Visualize Data
rides_dd = pd.read_csv('rides.txt')

import matplotlib.pyplot as plt

plt.scatter(rides_dd['duration'], rides_dd['distance'])

plt.show()