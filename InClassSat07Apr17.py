
# coding: utf-8

# In[6]:

import numpy as np
import pandas as pd


# In[11]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
                                         



# In[12]:

s


# In[13]:

s.index


# In[14]:

pd.Series(np.random.randn(5))


# In[15]:

d = {'a': 0., 'b': 1., 'c' : 2.}


# In[16]:

d


# In[19]:

pd.Series(d)


# In[20]:

pd.Series(d, index = ['b', 'c', 'd', 'a'])


# In[21]:

pd.Series(5., index ={'a', 'b', 'c', 'd', 'e'})


# In[22]:

s


# In[23]:

s[0]


# In[24]:

type(s)


# In[25]:

s[:3]


# In[26]:

s[s> s.median()]


# In[27]:

s[[4,3,1]]


# In[28]:

s[['a', 'b']]


# In[29]:

np.exp(s)


# In[30]:

s['e'] = 14


# In[31]:

s


# In[33]:

s['b', 'a'] = 12,11


# In[34]:

s


# In[35]:

'f' in s


# In[37]:

if 'e' in s:
    s['e'] = 13


# In[38]:

s


# In[39]:

s.get('f')


# In[42]:

s.get('f', np.nan)


# In[43]:

s+s


# In[44]:

s*3


# In[45]:

exp(s)


# In[47]:

s.append('f')


# In[48]:

s[1:]


# In[49]:

s[:-1]


# In[50]:

s[1:] +s[:-1]


# In[51]:

s = pd.Series (np.random.randn(5), name = 'something')
s


# In[53]:

s['f', 'g'] = 0, 12


# In[56]:

s['a', 'b'] = (0, 12)


# In[59]:

d = {'one' : pd.Series([1., 2., 3.], index = ['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index = ['a', 'b', 'c', 'd'])}


# In[60]:

d


# In[61]:

df = pd.DataFrame(d)


# In[62]:

df


# In[64]:

pd.DataFrame(d, index=['d', 'a'])


# In[67]:

pd.DataFrame(d, index = ['d', 'b', 'a'], columns = ['two', 'three'])


# In[68]:

d


# In[69]:

pd.DataFrame(d)


# In[70]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[71]:

data


# In[72]:

data[:] = [(1, 2., 'Hello'), (2, 3., 'World')]


# In[73]:

data


# In[76]:

data.A


# In[77]:

pd.DataFrame(data, index = ['first', 'second'])


# In[79]:

pd.DataFrame(data, index = ['first', 'second'], columns = ['C', 'A', 'B'])


# In[80]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]



# In[82]:

pd.DataFrame(data2, columns = ['a', 'f'])


# In[83]:

df


# In[84]:

df['one']


# In[85]:

df['three'] = df['one'] * df['two']


# In[86]:

df['three']


# In[87]:

df


# In[88]:

df['flag'] = df['one'] > 2


# In[89]:

df


# In[94]:

df


# In[95]:

two = df.pop('flag')


# In[96]:

two


# In[97]:

df = df.append(two)


# In[98]:

df


# In[99]:

df['another'] = 'bar'


# In[101]:

df[-'a']


# In[ ]:



