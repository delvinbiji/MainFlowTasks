#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('C:\\Users\\DELVIN BIJI\\Downloads\\heart.csv')


# In[3]:


#checking first five rows by calling df.head()
df.head()


# In[4]:


df.tail()


# In[5]:


df.columns.values


# In[6]:


df.isna().sum()


# In[7]:


#summary of dataset
df.info()


# In[8]:


#plotting histogram of all numeric values
df.hist(bins = 50, grid = False, figsize=(20,15));


# In[9]:


df.describe()


# In[10]:


questions = ["1. How many people have heart disease and how many people doesn't have heart disease?",
"2. People of which sex has most heart disease?",
"3. People of which sex has which type of chest pain most?",
"4. People with which chest pain are most pron to have heart disease?"]

questions


# In[11]:


#1. How many people have heart disease and how many people doesn't have heart disease?

df.target.value_counts()


# In[12]:


#plotting bar chart
df.target.value_counts().plot(kind= 'bar', color=["orchid", "salmon"])
plt.title("Heart Disease values")
plt.xlabel("1 Heart Disease, 6 No heart Disease")
plt.ylabel("Amount");


# In[13]:


#plotting pie chart
df.target.value_counts().plot(kind= 'pie', figsize = (8, 6))
plt.legend(["Disease", "No disease"]);


# In[14]:


# 0 - female
# 1 - male
#sex column
# 0 - no disease
# 1 - disease
df.sex.value_counts()


# In[15]:


#pie chart
df.sex.value_counts().plot(kind= 'pie', figsize = (8, 6))
plt.title('Male Female ratio')
plt.legend(['Male', 'Female']);


# In[16]:


# 2. People of which sex has most heart disease?
pd.crosstab(df.target, df.sex)


# In[17]:


sns.countplot(x = 'target', data = df, hue = 'sex')
plt.title("Heart Disease Frequency for Sex")
plt.xlabel("0 No heart Disease, 1 Heart Disease");


# In[18]:


# People of which sex has which type of chest pain most?
df.cp.value_counts()


# In[19]:


#plotting bar chart
df.cp.value_counts().plot(kind='bar', color=['salmon', 'lightskyblue', 'springgreen', 'khaki'])
plt.title('Chest pain type vs count');


# In[20]:


pd.crosstab(df.sex, df.cp)


# In[21]:


pd.crosstab(df.sex, df.cp).plot(kind='bar', color=['coral', 'lightskyblue', 'plum', 'khaki'])
plt.title('Type of chest pain for sex')
plt.xlabel('0 = Female, 1 = Male');


# In[22]:


# 4. People with which chest pain are most pron to have heart disease?
pd.crosstab(df.cp, df.target)


# In[23]:


sns.countplot(x = 'cp', data = df, hue = 'target');


# In[24]:


sns.displot(x = 'age', data = df, bins = 30, kde = True);


# In[25]:


# Maximum heart rate
sns.displot(x='thalach', data=df, bins=30, kde=True, color='chocolate');




