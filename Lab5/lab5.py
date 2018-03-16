# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:48:30 2018

@author: Matteo
"""
import pandas as pd 
import numpy
        


df =pd.read_csv("arrhythmia.data",sep=',',skiprows=29,header=None,na_values=['?','\t?',0])

df = df.dropna(axis=1,how='any')

#We want initially to separate class 1 (healthy people) from the other
#classes; so we define a new class 1 (healthy) and the new class 2
#(arrhythmic); we analyze the data twice

df2 = df.replace([3,4,5,6,7,8,9,10,11,12,13,14,15,16],2)

class_id = df2[279]
y = df2.drop(columns = 279)

y1 = df2.loc[df2[279] == 1]
y1 = y1.drop(columns = 279)
y2 = df2.loc[df2[279] != 1]
y2 = y2.drop(columns = 279)

x1 = y1.mean(axis = 0)
x2 = y2.mean(axis = 0)

#APPLYING MINIMUM DISTANCE CRITERION

h = []
s = []
for patient in list(y.index.values):
    #dist1 = abs(sum(y.loc[patient] - x1))
    #dist2 = abs(sum(y.loc[patient] - x2))
    
    dist1 = numpy.linalg.norm(y.loc[patient] - x1)
    dist2 = numpy.linalg.norm(y.loc[patient] - x2)
    
    
    if dist1 <= dist2:
        h.append(y.loc[patient])
    else:
        s.append(y.loc[patient])
        
pi1 = len(y1)/(len(y))
pi2 = len(y2)/len(y)
    
    
    