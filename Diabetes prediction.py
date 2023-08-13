#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


# In[4]:


diabetes_dataset=pd.read_csv(r'C:\Users\HP\Downloads\diabetes.csv')


# In[5]:


diabetes_dataset.head()


# In[6]:


diabetes_dataset.shape


# In[7]:


diabetes_dataset.describe()


# In[9]:


diabetes_dataset['Outcome'].value_counts()
#0-Non Diabetic
#1-Diabetic


# In[10]:


diabetes_dataset.groupby('Outcome').mean()


# In[11]:


X=diabetes_dataset.drop(columns='Outcome',axis=1)
Y=diabetes_dataset['Outcome']


# In[12]:


print(X)


# In[13]:


print(Y)


# In[14]:


scaler=StandardScaler()


# In[15]:


scaler.fit(X)


# In[16]:


standardised_data=scaler.transform(X)


# In[17]:


print(standardised_data)


# In[18]:


X=standardised_data
Y=diabetes_dataset['Outcome']


# In[19]:


print(X)
print(Y)


# In[20]:


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)


# In[21]:


print(X.shape,X_train.shape,X_test.shape)


# In[22]:


classifier=svm.SVC(kernel='linear')


# In[23]:


classifier.fit(X_train,Y_train)


# In[24]:


#accuracy score on training data
X_train_prediction=classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)


# In[25]:


print('Accuracy score= ',training_data_accuracy)


# In[26]:


#accuracy score on test data
X_test_prediction=classifier.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)


# In[27]:


print('Accuracy score= ',test_data_accuracy)


# In[31]:


input_data=(4,110,92,0,0,37.6,0.191,30)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
std_data=scaler.transform(input_data_reshaped)
print(std_data)
prediction=classifier.predict(std_data)
print(prediction)

if(prediction[0]==0):
    print('The person is not diabetic')
else:
    print('The person is diabetic')


# In[ ]:




