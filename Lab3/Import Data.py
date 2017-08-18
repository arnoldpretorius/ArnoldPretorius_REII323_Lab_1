# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 19:53:31 2017

@author: Arnold
"""
#task 1 Import a .csv file
import csv
filename="data.csv"
f=open(filename,"r")

#taks 2 Display  colum headers
c=csv.reader(f)
i=next(c)
print (i)

#taks 3 - Display first couple of rows to inspect formating
for i in range(5):
    j=next(c)
    print(j)
    
#task 4 - display file content to inspect file content
with open("data.csv") as g:
    reader = csv.reader(g)
    for row in reader:
        print(" ".join(row))



