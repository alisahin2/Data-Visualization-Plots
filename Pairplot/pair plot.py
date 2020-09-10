#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[31]:


iris = sns.load_dataset("iris")
iris.head()


# In[29]:


# genel bir gosterim
sns.pairplot(iris)


# In[30]:


# sekli renklendirme
sns.pairplot(iris, hue="species")


# In[32]:



sns.pairplot(iris, vars=["sepal_width", "sepal_length"])


# In[34]:


sns.pairplot(iris, 
             x_vars = ["sepal_length","sepal_width"],
             y_vars = ["petal_length","petal_width"],
            )


# In[ ]:




