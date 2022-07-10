#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re #regular expression
import pandas as pd
from matplotlib import dates
from datetime import datetime
f = open('WhatsApp Chat with BCA-DA2020.txt', 'r', encoding = 'utf-8')
data = f.read()

pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s'
messages = re.split(pattern, data)
messages = messages[1:]
type(messages)
print(messages)
dates = re.findall(pattern, data)
print(dates)
df = pd.DataFrame({'user_message': messages, 'message_date': dates})
# convert message_date type
df['message_date'] = pd.to_datetime(df['message_date'])
df.rename(columns={'message_date': 'date'}, inplace=True)
users = []
messages = []
for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
df['user'] = users
df['messages'] = messages
df.drop(columns=['user_message'], inplace= True)

df.head()
df['year'] = df['date'].dt.year
df.head()
df['month']= df['date'].dt.month_name()
df['day'] = df['date'].dt.day
df['hour'] = df['date'].dt.hour
df['minute']=df['date'].dt.minute
df.head(20)


# In[3]:


type(messages)


# In[4]:


type(dates)


# In[8]:


len(messages)


# In[21]:


len(dates)


# In[10]:


del(messages[0])


# In[19]:


messages = messages[1:]


# In[20]:





# In[18]:





# In[ ]:




