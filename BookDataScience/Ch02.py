#!/usr/bin/env python
# coding: utf-8

# In[3]:


a = 12
b = a*4
print(b)


# In[6]:


name='akkadate'
print(name,b)


# In[5]:


b = 512


# In[36]:


get_ipython().run_line_magic('pinfo', 'plt.bar')


# In[9]:


import matplotlib_inline as mp


# In[18]:


import IPython
print("IPthon version %6.6s (need at lease 1.0)" % IPython.__version__)


# In[16]:


import jupyterlab
print(" JupyterLab version %6.6s (need at lease 0.35.x)" % jupyterlab.__version__)


# In[26]:


#py -m pip install numpy
import numpy as np
print(" Numpy version %6.6s (need at lease 1.7.1)" % np.__version__)


# In[29]:


#py -m pip install xlrd
import xlrd
print(" xlrd version %6.6s (need at lease 1.0.0)" % xlrd.__version__)


# In[32]:


#py -m pip install pandas
import pandas as pd
print(" Pandas version %6.6s (need at lease 0.23.0)" % pd.__version__)


# In[35]:


#py -m pip install matplotlib
import matplotlib
print(" Matplotlib version %6.6s (need at lease 1.2.1)" % matplotlib.__version__)


# In[ ]:




