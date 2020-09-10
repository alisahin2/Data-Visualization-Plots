#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


# In[60]:


tips = sns.load_dataset("tips")
tips.head()


# In[47]:


vertical = sns.boxplot(x=tips["total_bill"])


# In[48]:


horizental = sns.boxplot(y=tips["total_bill"])


# In[49]:


sns.boxplot(x="day", y="total_bill", data=tips)


# In[61]:


sns.boxplot(x="day", y="total_bill", hue="sex",
                 data=tips, palette="Set1")


# In[62]:


sns.boxplot(x="time", y="tip", data=tips, order=["Dinner", "Lunch"])

