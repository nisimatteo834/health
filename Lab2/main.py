import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
if __name__=="__main__":
    
    #feat_names = pd.read_csv("chronic_kidney_disease.arff",nrows=4,header=2)
    feat_names = ['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','pcv','wbcc','rbcc','htn','dm','cad','appet','pe','ane','class']
    df=pd.read_csv("chronic_kidney_disease.arff",sep=',',skiprows=29,header=None,na_values=['?','\t?'],names=feat_names)
    
    #here i just drop the row having a NaN
    #todo substitution with a number

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
        
    
    
# =============================================================================
# You must first instantiate an object of that class, and then perform the
# training:
# clf = tree.DecisionTreeClassifier("entropy")
# clf = clf.fit(data, target)
# where data is the original Dataframe without the last column and target
# is the last column of the original Dataframe
# =============================================================================
    data = df.drop(labels='class',axis=1)
    target = df['class']
    
    clf = tree.DecisionTreeClassifier("entropy")
    clf = clf.fit(data,target)
    
    dot_data = tree.export_graphviz(clf,out_file="Tree.dot",feature_names=feat_names[0:24],class_names=feat_names[24],filled=True,rounded=True,special_characters=True)
#now run on the shell this    dot -Tpng Tree.dot -o Tree.png. Remember to open the shell in the current folder!
    print (clf)
