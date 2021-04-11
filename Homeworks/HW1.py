#!/usr/bin/env python
# coding: utf-8

# ### Create a List and swap the second half of the list with the first half of the list and print this list on the screen.

# In[76]:


liste = list(range(10))


# In[77]:


type(liste)


# In[78]:


liste


# In[79]:


type(liste)


# In[80]:


half1 = [int(i) for i in liste[:len(liste)//2]]
half2 = [int(i) for i in liste[len(liste)//2:]]


# In[81]:


half1


# In[82]:


half2


# In[83]:


type(half2)


# In[84]:


type(half1)


# In[85]:


liste = [half2 , half1]


# In[86]:


liste

