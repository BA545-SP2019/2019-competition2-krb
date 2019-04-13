# Imports and things
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.feature_selection import RFE
plt.style.use('ggplot')
pd.options.display.max_columns = None
    


def assign_age(Age):
    if Age >= 21 and Age <= 40:
        return "21-40"
    elif Age >= 41 and Age <= 60:
        return "41-60"
    elif Age >= 61:
        return "61+"
    
def make_model(df, df_target):
    
    
    X = df
    #y = df_target.values.ravel()
    y = df_target
    
    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=2019)
    
    # Begin oversampling
    oversample = pd.concat([X_train,y_train],axis=1)
    max_size = oversample['Default'].value_counts().max()
    lst = [oversample]
    
    for class_index, group in oversample.groupby('Default'):
        lst.append(group.sample(max_size-len(group), replace=True))
    X_train = pd.concat(lst)
    y_train=pd.DataFrame.copy(X_train['Default'])
    del X_train['Default']
    
    logreg = LogisticRegression()
    logreg.fit(X_train,y_train)
    y_pred=logreg.predict(X_test)
    
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    print(cnf_matrix)
    
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    print("Precision:",metrics.precision_score(y_test, y_pred))
    print("Recall:",metrics.recall_score(y_test, y_pred))
    
    
    
def rfe_select(df, df_target, num_features):
    dataset = df.values
    target = df_target.values.ravel()
    
    model = LogisticRegression()
    rfe = RFE(model, num_features)
    rfe = rfe.fit(dataset, target)
    print(rfe.ranking_)
    
    selected_cols = []
    cols_all = df.columns.tolist()
    for x in range(0,len(cols_all)):
        if(rfe.ranking_[x]==1):
            print(cols_all[x])
            selected_cols.append(cols_all[x])
    return(selected_cols)

def correlate(df,df_target,num_features, ignore_sign):
    df['Default'] = df_target
    non_ab = df[df.columns[:]].corr()['Default'][:-1]
    ab = df[df.columns[:]].corr()['Default'][:-1].abs()
    so = ab.sort_values(ascending=False)
    end_num = num_features - 1
    sort_list = so[0:end_num]

    if(ignore_sign == "True"):
        print (sort_list)
    else:
        print(non_ab)

