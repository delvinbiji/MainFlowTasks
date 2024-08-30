#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv('C:\\Users\\DELVIN BIJI\\Downloads\\householdtask3.csv')


# In[4]:


data.head(10)


# In[5]:


#Scatter plot with year against own
plt.scatter(data['year'], data['own'])

#Adding title to the plot
plt.title("Scatter plot")

#Setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the result
plt.show()


# In[6]:


#Line chart with year against own
plt.plot(data['year'])
plt.plot(data['own'])

#Adding title to the plot
plt.title("Line Chart")

#Setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the result
plt.show()


# In[7]:


#Bar chart or bar plot
plt.bar(data['year'], data['own'])

#Adding title to the plot
plt.title("Bar Chart")

#Setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the result
plt.show()


# In[8]:


#Histogram
plt.hist(data['income'])

plt.title("Histogram")

plt.show()


# In[ ]:




