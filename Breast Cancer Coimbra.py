#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


d=pd.read_csv('Breast  Cancer Coimbra.csv')
d


# In[3]:


d.head()


# In[4]:


d.tail()# for last 5 rows


# In[5]:


# shape --> no of rows and columns
d.shape


# In[6]:


d.columns


# # Indexing

# In[7]:


d['Age']


# In[8]:


d[['Age']]


# In[9]:


d.sample


# In[10]:


d['Leptin']


# In[11]:


d[['Leptin']]


# In[12]:


d[['Age','BMI']]


# In[13]:


type(d['Age'])


# In[14]:


d.info()


# In[15]:


d.describe()


# # Slicing

# In[16]:


d[67:70]


# In[17]:


d[::-1]


# In[18]:


d[::2]


# In[19]:


d[1:5]


# In[20]:


d[10:21]['Adiponectin']


# In[21]:


d[1:100][['Adiponectin','Age','Insulin']]


# In[22]:


d[1:100]['Age']


# ###
#     - loc--> integer/non integer
#     - iloc-->integer location-->integer

# In[23]:


d.loc[[10]]


# In[24]:


d.iloc[10:100]


# In[25]:


d.loc[100,'Resistin']


# In[26]:


d.loc[[100]]


# In[27]:


d[100:111]


# In[28]:


d.loc[100:111]


# In[29]:


d[100:110][['Age','HOMA','Resistin']]


# In[30]:


d.loc[1:10,'MCP.1']


# In[31]:


d.sum()


# In[32]:


d.sum()[['Age','HOMA']]


# In[33]:


d.max()


# In[34]:


d.mean()


# ## statical methods on data sets

# In[35]:


d.std()


# In[36]:


d.std()[['Resistin','MCP.1','Classification']]


# In[37]:


d.count()


# In[38]:


d.mode()


# In[39]:


d.median()


# In[40]:


d['Adiponectin'].var()


# In[41]:


d.var()


# In[42]:


d.min()['Glucose']


# In[43]:


d.mode()['Insulin']


# In[44]:


d['BMI'].var()


# # sorting:
#     - pd.sort_index()

# In[46]:


dir(pd)


# # row index
# d.sort_index(ascending=True)
# d

# In[48]:


d.sort_index(ascending=False)


# In[49]:


d.sort_index(axis=1,ascending=True)


# In[50]:


d.sort_index(axis=0,ascending=False)


# In[51]:


d.sort_values(by="Glucose",ascending=True)


# In[52]:


d.sort_values(by=["HOMA","Adiponectin"],ascending=True)


# In[53]:


d


# In[54]:


help(pd)


# # Filtering

# In[55]:


d


# In[56]:


d['HOMA'].max()


# In[57]:


d


# In[58]:


d[d['Leptin'] > 90]


# In[59]:


d[(d['Glucose'] > 90) & (d['Glucose'] < 150)]


# In[60]:


d[d['HOMA']>90].sum()


# # grouping

# In[62]:


d.shape


# In[63]:


d['HOMA'].unique()


# # plotting:
#     - import mataplotlib.pyplot as plt

# In[64]:


import matplotlib.pyplot as plt


# In[65]:


d.plot()


# In[66]:


d['Glucose'].plot()


# In[67]:


d[['HOMA','Resistin']].plot()


# In[68]:


r=d.reset_index()


# In[69]:


r


# # Seaborn

# In[71]:


import seaborn as s


# In[79]:


s.catplot(x="Leptin",y="Glucose",data=d)


# In[80]:


s.jointplot(x="Leptin",y="Glucose",data=d)


# In[84]:


g=d.corr()
s.pairplot(g)


# In[ ]:




