import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


if __name__=="__main__":
    
    #feat_names = pd.read_csv("chronic_kidney_disease.arff",nrows=4,header=2)
    
    x=pd.read_csv("chronic_kidney_disease.arff",sep=',',skiprows=29,header=None,na_values=['?','\t?'],names=['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','pcv','wbcc','rbcc','htn','dm','cad','appet','pe','ane','class'])
