# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:56:16 2019

@author: 503143587
"""

import pandas as pd
import os

data_folder = '201910-citibike-tripdata'
data_file = '201910-citibike-tripdata.csv'
data_path = os.path.join(os.getcwd(), data_folder, data_file)
data = pd.read_csv(data_path)

