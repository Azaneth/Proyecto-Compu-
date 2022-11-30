#!/usr/bin/env python
# coding: utf-8

# # Proyecto 
# ***Física Computacional***
# 
# 
# **Azaneth González Domínguez**
# 
# _30/11/22_

# In[1]:


import pandas as pd
from pylab import *


# In[2]:


df = pd.read_csv('F0001CH2.csv')
print(df.to_string())


# In[7]:


data = pd.read_csv('F0001CH2.csv')
dx = pd.DataFrame(data, columns=['x', 'valor'])
print(df)


# In[8]:


figure(dpi=200)
n=np.linspace(0,11,11)
plt.title("Pulsos prueba")
plt.plot(dx)
plt.xlabel('dx')
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




