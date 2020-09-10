#!/usr/bin/env python
# coding: utf-8

# In[8]:


#
import seaborn as sns
import matplotlib.pyplot as plt
ds = sns.load_dataset("tips")


# In[9]:


ds.head()


# In[12]:


sns.scatterplot(x = "tip", y = "total_bill", data = ds)


# In[14]:


sns.scatterplot(x = "tip", y = "total_bill", data = ds, hue = "sex")


# In[20]:


sns.scatterplot(
    x = "total_bill",
    y = "tip",
    hue = "day",
    style = "time",
    data = ds
)


# In[ ]:




