# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 20:27:08 2017

@author: Arnold
"""

#task 5 - save columns 1,3 and 5 to new csv file
import csv
fl=open("data.csv","r") #open input file for reading
users_dict = {}
with open('reduced.csv','wb') as f: #output csv file
    writer = csv.writer(f)
    with open('data.csv','r') as csvfile: #input csv file
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            j=row[0],row[2],row[4]
            print (j)
        
fl.close()