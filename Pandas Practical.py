#!/usr/bin/env python
# coding: utf-8

# # Pandas tutorial

# * it is a powerful python data analysis toolkit
# * A fast and efficient Dataframe object for data manipulation
# * we can read and write : csv , txt , xml , json , zip etc

# ## Pandas Data structure

# * **Series** : one dimentional homogeneous labelled data
# * **DataFrame** : Two dimentional hetrogeneous tabular structure
# * **panel** : three dimentional lebelled data 

# ### Series

# In[2]:


import pandas as pd
list1 = [1,2,3,4,5]
s1 = pd.Series(list1 , dtype = int)


# In[3]:


print(s1)


# In[4]:


S1 = pd.Series(list1 , ["a","b","c","d","e" ], dtype = int ,  name = "data points")
print(S1)
print(type(S1))


# In[5]:


S1["c"]


# In[6]:


s2 = pd.Series([1,2,3,4,5])


# In[7]:


s2


# ### DataFrame

# ### Handling missing values

# In[8]:


neeraj = pd.read_csv("C://Users//Prem//Desktop//Water Quality//water_potability.csv")
neeraj.head()


# In[9]:


df1 = pd.read_csv("titanic.csv")
df1


# In[10]:


df1.shape


# In[12]:


df1.head(2)


# In[ ]:


df1.tail()


# In[ ]:


df1.describe()


# In[ ]:


df1.info()


# In[ ]:


df1.isnull().sum() ## it will find missing values in columns


# In[ ]:


df1 = df1.dropna() ## drop rows in which we have missing values


# In[ ]:


df1.shape


# In[ ]:


df1.isnull().sum()


# In[ ]:


df1.columns


# In[ ]:


df1.drop("survived" ,axis = 1 )


# In[ ]:


df1.head()


# ### Fillna()

# In[ ]:


df1 = pd.read_csv("titanic.csv" )


# In[ ]:


df1.head(10)


# In[ ]:


df1.fillna("neha" , inplace = True)


# In[ ]:


df1.head()


# In[ ]:


df1["deck"].fillna("abc" , inplace=True)


# In[ ]:


df1.head(10)


# In[ ]:


df1[["deck", "age"]] = df1[["deck", "age"]].fillna("ab")
df1.head(10)


# In[ ]:


df1[["deck", "age" , "fare" , "sibsp"]]


# In[ ]:


df1 = df1.fillna({"deck": "neha" , "age" : 28 })


# In[ ]:


df1.head(10)


# In[ ]:


df1.to_excel("prem.xlsx")


# ### Replace()

# In[ ]:


df2 = pd.read_csv("titanic.csv" )
df2.head()


# In[ ]:


df2.replace( "male" ,"female" , inplace = True)


# In[ ]:


df2.head()


# In[ ]:


df2["class"].replace("Third" , "Five"  , inplace = True)


# In[ ]:


df2["alone"].replace({False : True , True : False} , inplace = True )


# In[ ]:


df2.head()


# In[ ]:


df2.replace("male", "female" , inplace = True)
df2.head()


# In[ ]:


df2["age"] = df2["age"].replace(22.0 , 26.0)
df2.head(10)


# In[ ]:


df2["pclass"].replace({1 : 0 , 3 : 0 , 2 : 0} , inplace = True)


# In[ ]:


df2.head(10)


# In[ ]:


df2 = df2.replace("[A-Za-z]" , 0 , regex= True)
df2.head()


# ###  iloc

# In[ ]:


df3 = pd.read_csv("SalaryGender.csv")
df3


# In[ ]:


df3.shape


# In[ ]:


df3.iloc[0]


# In[ ]:


df3.iloc[:,:]


# In[ ]:


df3.iloc[:,:-1]


# In[ ]:


df3.head(10)


# In[ ]:


df3.iloc[2:5,1:3]


# ### Groupby()

# In[ ]:


df3


# In[ ]:


gr = df3.groupby(by = "Gender")


# In[ ]:


gr.groups


# In[ ]:


for a , b in gr:
    print(a)
    print(b)


# In[ ]:


gr.mean()


# In[ ]:


gr.sum()


# ### Concat()

# In[ ]:


df6 =pd.DataFrame(({"ID" : [1,2,3,4],
       "Name" : ["a", "b","c", "d"],
       "Class" : [5,6,7,8],
        "marks" :[10 , 20 , 30 , 40]}))


# In[ ]:


df6.head()


# In[ ]:


df7 =pd.DataFrame({"ID" : [1,2,3,4 , 5],
       "Name" : ["e", "f","g", "h" , "e"],
       "Class" : [9,10,11,12 , 7],
        "marks" : [50 , 60 , 70 , 80 , 90]})


# In[ ]:


df7.head()


# In[ ]:


data = pd.concat([df6,df7] , axis = 0) ### column wise


# In[ ]:


data


# In[ ]:


pd.concat([df7,df6] , axis = 1)


# ### Pivot_table()

# In[ ]:


df8 = pd.read_csv("SalaryGender.csv" )
df8.head()


# In[ ]:


df8.pivot_table(index = "Gender" , aggfunc="mean")


# In[ ]:


df8.pivot_table(index = "Gender" , columns = "PhD" , aggfunc = "mean" )


# In[ ]:





# In[ ]:




