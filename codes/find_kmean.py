#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
from sklearn.cluster import KMeans
FILENAME_cost = "/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/dataset/medicalcost/processed_medicalcost.csv"
FILENAME_mice = "/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/dataset/mice protein/Data_Cortex_Nuclear.csv"
df_mice = pd.read_csv(FILENAME_mice)
df_cost = pd.read_csv(FILENAME_cost)


# In[13]:


df_mice.drop("MouseID", axis=1, inplace=True)


# In[14]:


df_mice.describe()


# In[16]:


df_mice.drop("Treatment", axis=1, inplace=True)
df_mice.drop("Behavior", axis=1, inplace=True)
df_mice.drop("class", axis=1, inplace=True)


# In[22]:


df_cost.drop("Unnamed: 0", axis=1, inplace=True)
df_cost.drop("charges", axis=1, inplace=True)


# In[20]:


from sklearn.cluster import KMeans
print("Dataset: medical cost")
for k in range (1, 11):
    # Create a kmeans model on our data, using k clusters. random_state helps 
    # ensure that the algorithm returns the same results each time.
    kmeans_model = KMeans(n_clusters=k, random_state=1).fit(df_cost.iloc[:, :])
    # These are our fitted labels for clusters -- the first cluster has label 0, 
    # and the second has label 1.
    labels = kmeans_model.labels_
    # Sum of distances of samples to their closest cluster center
    interia = kmeans_model.inertia_
    if k == 1:
        reduced_cost = 0
        last_cost = interia
    else:
        reduced_cost = last_cost - interia
        last_cost = interia
    print("k: " + str(k) + "; cost: " + str(interia) + "; reduced: " + str(reduced_cost))


# In[41]:


print("Dataset: mice proteins")
for k in range (1, 11):
    # Create a kmeans model on our data, using k clusters. random_state helps 
    # ensure that the algorithm returns the same results each time.
    kmeans_model = KMeans(n_clusters=k, random_state=1).fit(df_mice.iloc[:, :])
    # These are our fitted labels for clusters -- the first cluster has label 0, 
    # and the second has label 1.
    labels = kmeans_model.labels_
    # Sum of distances of samples to their closest cluster center
    interia = kmeans_model.inertia_
    if k == 1:
        reduced_cost = 0
        last_cost = interia
    else:
        reduced_cost = last_cost - interia
        last_cost = interia
    print("k: " + str(k) + "; cost: " + str(interia) + "; reduced: " + str(reduced_cost))


# In[27]:


df_mice.dtypes


# In[26]:


df_mice.drop("Genotype", axis=1, inplace=True)


# In[30]:


df_mice.isnull().any()


# In[31]:


df_mice.apply(lambda x: x.fillna(x.mean()),axis=0)


# In[32]:


df_mice.isna().any()


# In[36]:


df_mice.isnull().any()


# In[35]:


df_mice.fillna(df_mice.mean()).dropna(axis=1, how='all')


# In[40]:


df_mice.columns[df_mice.isna().any()].tolist()


# In[39]:


df_mice.apply(lambda x: x.fillna(x.mean(), inplace=True),axis=0)


# In[ ]:




