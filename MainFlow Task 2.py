#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r'C:\Users\DELVIN BIJI\Downloads\01.Data Cleaning and Preprocessing.csv')


# In[5]:


print(df.columns)


# In[13]:


# Filtering based on conditions
filtered_df = df[df['BF-CMratio'] > 30]
print(filtered_df)


# In[15]:


# Dropping Missing Values
# Drop rows with any missing values:
df.dropna(inplace=True)
df


# In[16]:


# Drop columns with any missing values
df.dropna(axis=1, inplace=True)
df


# In[18]:


# filling missing values
# Fill with a specific value
df.fillna(value=0, inplace=True)
df


# In[19]:


# Fill with the mean of a column
df['ChipRate'].fillna(df['ChipRate'].mean(), inplace=True)
df


# In[20]:


# Fill with a forward fill (previous value)
df.fillna(method='ffill', inplace=True)
df


# In[22]:


# Calculating Summary Statistics
# Mean
mean_BlowFlow = df['BlowFlow'].mean()
print(mean_BlowFlow)


# In[23]:


# Median
median_BlowFlow = df['BlowFlow'].median()
print(median_BlowFlow)


# In[24]:


# Sum
total_BlowFlow = df['BlowFlow'].sum()
print(total_BlowFlow)


# In[26]:


BlowFlow_counts = df['BlowFlow'].value_counts()
print(BlowFlow_counts)


# In[27]:


# Descriptive statistics
df.describe()


# In[28]:


df.dtypes


# In[ ]:




