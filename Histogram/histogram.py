#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np, pandas as pd, seaborn as sns, import matplotlib.pyplot


# In[35]:


ds = sns.load_dataset("iris")
ds.head()


# In[36]:


ds.hist()


# In[55]:


ds.hist("petal_width")


# In[59]:


nums = np.random.randint(500,10000,250)
nums


# In[60]:


p = pd.DataFrame(nums)
p


# In[61]:


one = sns.distplot(p)


# In[62]:


two = sns.distplot(p, rug=True)


# In[63]:


three = sns.distplot(p, rug=True, hist=False)


# In[ ]:




