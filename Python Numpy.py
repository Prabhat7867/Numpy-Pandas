#!/usr/bin/env python
# coding: utf-8

# ## Numpy tutorials

# * its a general- purpose array processing package
# * It is a scientific computing library for python
# * Support large no. of data in the form of multi-dimentional array and matrix
# * Use for mathematical calculation like linear algebra , fourier transform etc.

# An array is a data structure that stores some value of same data type . In python, this is the main difference between lists and arrays. while python list can contain values corresponding to different data types , arrays in python can only contain values corresponding to same data type

# In[2]:


import numpy as np


# In[3]:


a = list(range(1,11))


# In[4]:


abc = np.array(a)


# In[5]:


abc


# In[6]:


type(abc)


# In[7]:


n = np.array(range(2 , 11 , 2)) ## Start : end : step


# In[8]:


n


# In[9]:


a = np.array([5 , 6 , 7 , "prem"])
a


# In[10]:


arr_1 = np.array([1,2,3,4,5,6])
arr_1


# In[11]:


type(arr_1)


# In[12]:


print(arr_1.ndim)


# In[13]:


arr2 = np.array([[1,2,3] , [5 , 6 , 7], [7 , 8 , 9]] , dtype = "str")
arr2


# In[14]:


print(arr2.size)
print(arr2.ndim)
print(arr2.shape)
print(arr2.dtype)


# In[15]:


once = np.ones(5, dtype = int)
once


# In[16]:


type(once[3])


# In[17]:


ones = np.ones((4,7) , dtype = float)
print(ones)


# In[18]:


zeros = np.zeros((2,4) ,dtype = int)
print(zeros)
print(zeros.ndim)


# ## Arange()

# In[19]:


#  np.arange(start , end , steps)
b = np.arange(1,5)
print(b)
print(type(b))
print(b.ndim)


# In[20]:


n = np.arange(1,13,2)
print(n)


# In[21]:


arr_1d = np.arange(1,13)
print(arr_1d)
arr_1d.ndim


# ## linspace()

# In[22]:


np.linspace(1 , 5 , 8)# it will create equal space between numbers


# ## Reshape()

# In[23]:


arr_1d


# In[24]:


arr_2 = arr_1d.reshape(4 , 3) 
print(arr_2)


# In[25]:


arr_3 = arr_1d.reshape(2,2,3)
print(arr_3)
print(arr_3.ndim)


# ## flatten()

# In[26]:


arr_2.flatten() # it will create multi-dimentional array into 1 D array


# In[27]:


arr_3d = np.arange(1 , 13).reshape(2,2,3)
arr_3d.flatten()


# In[28]:


arr_3d


# ## transpose()

# In[29]:


arr_2


# In[30]:


arr_2 = arr_2.transpose()
# arr_2 = arr_2.T


# In[31]:


arr_2


# In[32]:


arr_2.shape


# In[33]:


arr1 = np.arange(1,13).reshape(3,4)
arr1


# In[34]:


arr2 = np.arange(1,13).reshape(3,4)
arr2


# In[35]:


arr1 + arr2


# In[36]:


arr1 / arr2


# In[37]:


arr1 * arr2


# In[38]:


np.multiply(arr1 , arr2)


# In[ ]:


arr1


# In[40]:


arr1 @ arr2.T


# In[41]:


arr1.dot(arr2.T)


# In[42]:


arr1


# In[49]:


max(arr1.flatten())


# In[45]:


arr1.max(axis = 0) # max of columns


# In[46]:


arr1.max(axis = 1) # max of rows


# In[47]:


np.sum(arr1)


# In[51]:


np.sum(arr1 , axis = 1)


# In[52]:


np.mean(arr1)


# In[53]:


np.cbrt(arr1)


# In[69]:


arr1**3


# In[55]:


np.std(arr1)


# In[56]:


np.exp(arr1)


# In[57]:


np.log(arr1)


# In[58]:


np.log10(arr1)


# In[59]:


mx = np.arange(1,101).reshape(10,10)
mx


# In[60]:


mx[4,3] # rows * column


# In[63]:


mx[5,6]


# In[64]:


mx[4,3].ndim


# In[65]:


mx.ndim


# In[66]:


mx[:,:]


# In[67]:


mx[4:7 , 6 :9]


# In[ ]:




