# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:05:08 2018

@author: Matteo
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from sklearn import tree
from scipy.cluster.hierarchy import dendrogram,linkage
import matplotlib
if __name__=="__main__":
    
    random.seed(1000)
    #feat_names = pd.read_csv("chronic_kidney_disease.arff",nrows=4,header=2)
    feat_names = ['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','pcv','wbcc','rbcc','htn','dm','cad','appet','pe','ane','class']
    df=pd.read_csv("chronic_kidney_disease.arff",sep=',',skiprows=29,header=None,na_values=['?','\t?'],names=feat_names)
    df.to_csv('strings.csv',sep=',')
    df = df.dropna(axis=0)
    df = df.replace('yes',1)
    df = df.replace('no',0)
    df = df.replace('ckd',1)
    df = df.replace('notckd',0)
    df = df.replace('normal',1)
    df = df.replace('abnormal',0)
    df = df.replace('good',1)
    df = df.replace('poor',0)
    df = df.replace('present',1)
    df = df.replace('notpresent',0)        
    	
    df.to_csv('tocsv.csv',sep=',')
