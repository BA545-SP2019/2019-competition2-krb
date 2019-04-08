# Imports and things
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
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
    
    
    X = df.values
    y = df_target.values.ravel()
    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=2019)
    
    logreg = LogisticRegression()
    logreg.fit(X_train,y_train)
    y_pred=logreg.predict(X_test)
    
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    print(cnf_matrix)
    
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    print("Precision:",metrics.precision_score(y_test, y_pred))
    print("Recall:",metrics.recall_score(y_test, y_pred))
    
    
    
    