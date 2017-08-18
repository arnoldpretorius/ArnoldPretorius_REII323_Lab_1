# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 20:49:26 2017

@author: Arnold
"""

#Task 6 Merge two datasets on the timestamp field
import pandas as pd
a = pd.read_csv("LoadData.csv"); #load file 1
b = pd.read_csv("WeatherData.csv") #load file 2
merged = a.merge(b, on="TimeStamp")
merged.to_csv("merged.csv",index=False)

import csv
f2 = open("merged.csv","r")
l = csv.reader(f2)
m = next(l)

print(m)