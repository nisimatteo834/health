import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import subprocess as sp
import os
from sklearn import tree
if __name__=="__main__":
       
    random.seed(1000)
    np.random.seed(50)
    #feat_names = pd.read_csv("chronic_kidney_disease.arff",nrows=4,header=2)
    folder = "C:\\Users\\Matteo\\Desktop\\lab_second_year\\Lab2\\"
    #folder =  os.path.dirname(os.path.realpath(__file__)) + "\\"
    feat_names = ['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','pcv','wbcc','rbcc','htn','dm','cad','appet','pe','ane','class']
    df=pd.read_csv(folder+"chronic_kidney_disease.arff",sep=',',skiprows=29,header=None,na_values=['?','\t?'],names=feat_names)
    
    #here i just drop the row having a NaN
    #todo substitution with a number

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

    
    df = df.dropna(axis=0)

        
#%%
    
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
    clf = tree.DecisionTreeClassifier("entropy",max_features=1)
    clf = clf.fit(data,target)
    classes = ['notckd','ckd']
    dot_data = tree.export_graphviz(clf,out_file="Tree.dot",feature_names=feat_names[0:24],class_names=classes,filled=True,rounded=True,special_characters=True)
    input_name = "Tree.dot"
    output_name = "Tree.png"
    png = sp.run(['dot', '-Tpng', input_name, '-o', output_name], stdout=sp.PIPE, shell = True)
    print(png.stdout.decode('utf-8'))
    
    
    import matplotlib.pyplot as plt
    import matplotlib.image as mplimg
    plt.figure(figsize = (45,15))
    img = mplimg.imread('Tree.png')
    imgplot = plt.imshow(img)
    plt.show()
    
    #%%
    df=pd.read_csv("chronic_kidney_disease.arff",sep=',',skiprows=29,header=None,na_values=['?','\t?'],names=feat_names,usecols=range(0,25))
    df = df.fillna(-1)
    count = 0
    for char in ['',' ','\t']:
        if char == ' ' or char == '\t':
            count = count +1
        df = df.replace(char + 'yes',1)
        df = df.replace(char + 'no',0)
        df = df.replace(char +'ckd',1)
        df = df.replace(char+'notckd',0)
        df = df.replace(char+'normal',1)
        df = df.replace(char+'abnormal',0)
        df = df.replace(char+'good',1)
        df = df.replace(char+'poor',0)
        df = df.replace(char+'present',1)
        df = df.replace(char+'notpresent',0)    
    for char in ['',' ','\t']:
        if char == ' ' or char == '\t':
            count = count +1
        df = df.replace('yes'+char ,1)
        df = df.replace('no'+char,0)
        df = df.replace('ckd'+char,1)
        df = df.replace('notckd'+char,0)
        df = df.replace('normal'+char,1)
        df = df.replace('abnormal'+char,0)
        df = df.replace('good'+char,1)
        df = df.replace('poor'+char,0)
        df = df.replace('present'+char,1)
        df = df.replace('notpresent'+char,0)    
    
    random.seed(1000)
    np.random.seed(50)
    
    data = df.drop(labels='class',axis=1)
    target = df['class']
    clf = tree.DecisionTreeClassifier("entropy",max_features=1)
    clf = clf.fit(data,target)
    classes = ['notckd','ckd']
    dot_data = tree.export_graphviz(clf,out_file="Tree_2.dot",feature_names=feat_names[0:24],class_names=classes,filled=True,rounded=True,special_characters=True)
    input_name = folder + "Tree_2.dot"
    output_name = folder + "Tree_2.png"
    png2 = sp.run(['dot', '-Tpng', input_name, '-o', output_name], stdout=sp.PIPE, shell = True)
    print(png.stdout.decode('utf-8'))
    
    
    import matplotlib.pyplot as plt
    import matplotlib.image as mplimg
    img = mplimg.imread('Tree_2.png')
    plt.figure(figsize = (45,15))
    imgplot = plt.imshow(img)
    plt.show()
    

 
#now run on the shell this    dot -Tpng Tree.dot -o Tree.png. Remember to open the shell in the current folder!
