#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd


# In[13]:


isimler = ["ali", "veli", "semih", "aysegul"]
yaslar = [10,20,30,35]


# In[14]:


# dict ekleme
veri = {'name': pd.Series(isimler), 'age': pd.Series(yaslar)}
df = pd.DataFrame(veri)
df


# In[15]:


df.plot.bar()


# In[16]:


df.index


# In[17]:


salary = [1000,2000,1500,3000]
df['Salary'] = pd.Series(salary)
df


# In[34]:


df.plot.bar()


# In[31]:


import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))


# In[28]:


import matplotlib
matplotlib.style.use('seaborn-whitegrid')


# In[39]:


df[["Salary"]].plot.bar()


# In[48]:


df[["Salary","age"]].plot.bar(x='age')

