#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split 


#binary classification. 0=CN, 1=MCI/AD
dataset = pd.read_csv("C:\\Users\\AZD\\Desktop\\merged_normalized_4_COPY1_COPY2.csv", header=0) # merged_normalized_4_COPY1
# dataset = pd.read_csv("C:\\Users\\AZD\\Desktop\\boxplot_validation_set.csv", header=0)
dataset=dataset.dropna()

# merged normalized_4
X = dataset.iloc[:, 0:22]
y = dataset.iloc[:, 23]

# dividing X, y into train and test data 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) 

# training a KNN classifier 
from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors = 7).fit(X_train, y_train) 
  
# accuracy on X_test 
accuracy = knn.score(X_test, y_test) 
print("KNN Model accuracy: ", accuracy)
  
# creating a confusion matrix 
knn_predictions = knn.predict(X_test)  
cm = confusion_matrix(y_test, knn_predictions)

# this is where we would take the form inputs and add it to this new_input array. It must be in a specific order. For values that are not filled out, I think we put NaN.
new_input = [[57.8,0,1,1,15,7,0.375,0.277777777777778,0.285714285714286,0.25,0.4,0.375,0.909090909090909,0.075,0.173076923076923,0.100469439997525,0.446612830865859,0.6,0.33799248307702,0.488164816360999,0.356406253240232,0.066666666666667]]
output = knn.predict(new_input)
print("classification of input: ", output) #this is the classification. 0=CN, 1=MCI/AD


# In[ ]:




