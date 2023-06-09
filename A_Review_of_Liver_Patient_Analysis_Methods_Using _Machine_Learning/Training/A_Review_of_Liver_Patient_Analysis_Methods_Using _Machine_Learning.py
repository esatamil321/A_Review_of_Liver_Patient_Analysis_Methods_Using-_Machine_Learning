# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14Qnh7L-qWFNOsLonUmbkdw9oecAoV8Vv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
#import the dataset from specified location
data = pd.read_csv('/content/indian_liver_patient.csv')
# showing the data from top 5
data.head()

data.tail()

data.describe()

data.info()

data.isnull().any()

data.isnull().sum()

data[data['Dataset']==1]

data['Dataset'].unique()

#checking for missing data
data.isnull().sum()

data['Albumin_and_Globulin_Ratio'].fillna(data['Albumin_and_Globulin_Ratio'].mode()[0], inplace=True)

data['Albumin_and_Globulin_Ratio'].fillna(data['Albumin_and_Globulin_Ratio'].mode()[0], inplace=True)
data.isnull().sum()

plt.figure(figsize=(15,10))
plt.subplot(3,3,1)
plt.scatter(data['Age'], data['Dataset'])
plt.ylabel('Dataset')
plt.xlabel('Age')

plt.subplot(3,3,2)
plt.scatter(data['Gender'], data['Dataset'])
plt.ylabel('Dataset')
plt.xlabel('Gender')

plt.subplot(3,3,3)
plt.scatter(data['Total_Bilirubin'], data['Dataset'])
plt.ylabel('Dataset')
plt.xlabel('Total_Bilirubin')

plt.subplot(3,3,4)
plt.scatter(data['Direct_Bilirubin'], data['Dataset'])
plt.ylabel('Dataset')
plt.xlabel('Direct_Bilirubin')

plt.subplot(3,3,5)
plt.scatter(data['Alkaline_Phosphotase'], data['Dataset'])
plt.ylabel('Dataset')
plt.xlabel('Alkaline_Phosphotase')

plt.subplot(3,3,6)
plt.scatter(data['Alamine_Aminotransferase'], data['Dataset'])
plt.ylabel('Dataset')
plt.xlabel('Alamine_Aminotransferase')

plt.subplot(3,3,7)
plt.scatter(data['Aspartate_Aminotransferase'], data['Dataset'])
plt.ylabel('Dataset')
plt.xlabel('Aspartate_Aminotransferase')

plt.subplot(3,3,8)
plt.scatter(data['Total_Protiens'], data['Dataset'])
plt.ylabel('Dataset')
plt.xlabel('Total_Protiens')

plt.subplot(3,3,9)
plt.scatter(data['Albumin_and_Globulin_Ratio'], data['Dataset'])
plt.ylabel('Dataset')
plt.xlabel('Albumin_and_Globulin_Ratio')

sns.countplot(data=data, x = 'Dataset')
LD,NLD=data['Dataset'].value_counts()
print("liver disease patinets:",LD)
print("Non-liver disease patinets:",NLD)

sns.countplot(data=data, x = 'Gender', label='Count')
m,f=data['Gender'].value_counts()
print("No of Males:",m)
print("No of Females:",f)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
# Converting Textual data into numeric data
data['Gender'] = le.fit_transform(data['Gender'])
data.head()

data['Gender'] = le.fit_transform(data['Gender'])

data.head()

x=data.iloc[:,0:-1]
y=data.iloc[:,-1]
# dividing the data into input and output
x=data.iloc[:,0:-1]
y=data.iloc[:,-1]
# importing the train_test_split from scikit-learn
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)
# Returns size of xtrain 
xtrain.shape

xtest.shape

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# Importing the machine learning model
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

svm=SVC()
RFmodel=RandomForestClassifier()
KNNmodel=KNeighborsClassifier()

from sklearn.svm import SVC
svm=SVC()

svm.fit(xtrain, ytrain)

SVMpred=svm.predict(xtest)

SVMaccuracy=accuracy_score(SVMpred, ytest)
SVMaccuracy

SVMcm=confusion_matrix(SVMpred, ytest)
SVMcm

from sklearn.ensemble import RandomForestClassifier
RFmodel=RandomForestClassifier()
# train the data with Random Forest model
RFmodel.fit(xtrain, ytrain)

RFpred=RFmodel.predict(xtest)
# Checking for accuracy score from actual data and predicted data
RFaccuracy=accuracy_score(RFpred, ytest)
RFaccuracy

RFcm=confusion_matrix(RFpred, ytest)
RFcm

# K-Nearest Neighbors Model
from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier()
# train the data with K-Nearest Neighbors Model
KNN.fit(xtrain, ytrain)

KNNpred=KNN.predict(xtest)
# Checking for accuracy score from actual data and predicted data
KNNaccuracy=accuracy_score(KNNpred, ytest)
KNNaccuracy

# showing the confusion matrix
KNNcm=confusion_matrix(KNNpred, ytest)
KNNcm

print("Support Vector Machine Algorithm accuracy score : {value:.2f} %".format(value=SVMaccuracy*100))
print("Random Forest Algorithm accuracy score : {value:.2f} %".format(value=RFaccuracy*100))
print("K-Nearest Neighbors Algorithm accuracy score : {value:.2f} %".format(value=KNNaccuracy*100))

# saving the model
import pickle
pickle.dump(svm, open('liver_analysis.pkl','wb'))

pip install pipreqs