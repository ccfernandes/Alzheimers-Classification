#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# file includes functions used to process Flask form input for the model --> normalization 
# AND
# the model itself

import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split 

#pass in the imaging variables. we may just want to make them global somehow
void normalize_imaging(float icv, float cerebrum, float ventricle, float hippo, float entorhinal):
    cerebrum = cerebrum / icv
    ventricle = ventricle / icv
    hippo = hippo / icv
    entorhinal = entorhinal / icv

#file path depends on where its located in the flask project
void train_RF():
    dataset = pd.read_csv("C:\\Users\\AZD\\Desktop\\boxplot_validation_set.csv", header=0)
    dataset=dataset.dropna()
    X = dataset.iloc[:, 0:21]
    y = dataset.iloc[:, 22]
    
    # dividing X, y into train and test data 
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) 

    # training a DescisionTreeClassifier 
    from sklearn.tree import DecisionTreeClassifier 
    dtree_model = DecisionTreeClassifier(max_depth = 4).fit(X_train, y_train) 
    dtree_predictions = dtree_model.predict(X_test)
    
#file path depends on where its located in the flask project

# input formInput is an array with all of the submitted form data from the frontend
void run_RF(formInput):
    dataset = pd.read_csv("C:\\Users\\AZD\\Desktop\\boxplot_validation_set.csv", header=0)
    dataset=dataset.dropna()
    X = dataset.iloc[:, 0:21]
    y = dataset.iloc[:, 22]
    
    # dividing X, y into train and test data 
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) 

    # training a DescisionTreeClassifier 
    from sklearn.tree import DecisionTreeClassifier 
    dtree_model = DecisionTreeClassifier(max_depth = 4).fit(X_train, y_train) # make this a global variable so you can just use dtree_model rather than having to train it again. 
    
    output = dtree_model.predict(new_input)
    print("classification: ", output)

