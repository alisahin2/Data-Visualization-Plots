#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
tips = sns.load_dataset("tips")
tips


# In[4]:


empty = sns.FacetGrid(tips)


# In[5]:


one = sns.FacetGrid(tips, col="time", row="smoker")


# In[6]:


import matplotlib.pyplot as plt


# In[ ]:


sns.FacetGrid(tips)

