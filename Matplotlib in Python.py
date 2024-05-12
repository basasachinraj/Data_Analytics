#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


table = pd.read_csv('HistoricalPrices.csv',
                   header=0,
                   )
table.head()


# In[4]:


table.info()


# In[194]:


table['Date'] = pd.to_datetime(table['Date'])


# In[6]:


table = table.sort_values(by='Date')


# In[7]:


table


# In[8]:


table = table.rename(columns = {' Open': 'Open', ' High': 'High', ' Low': 'Low', ' Close': 'Close'})


# In[9]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime


# In[181]:


plt.plot(table['Date'], table['Close'], color='green')
plt.title('Close Value by Date')
plt.show()


# In[182]:


plt.plot(table['Date'], table['Close'])
plt.plot(table['Date'], table['Open'])
plt.title('Open and close value by date')
plt.show()


# In[12]:


plt.plot(table['Date'], table['Close'], label = 'Close')
plt.plot(table['Date'], table['Open'], label = 'Open')
plt.title('Open and close value by date')
plt.legend()
plt.show()


# In[13]:


from calendar import month_name


# In[125]:


table['Month'] = pd.Categorical(table['Date'] .dt.month_name(), month_name[1:])


# In[15]:


table


# In[183]:


plt.bar(table['Month'], height = table['High'], color='green')
plt.ylim(39000,40000)
plt.title('High value by Month')
plt.show()


# In[190]:


plt.barh(table['Month'],table['High'])
plt.xlim(38000,40000)
plt.title('High value by Month')
plt.show()


# In[191]:


plt.scatter(table['Open'], table['Close'], color= 'red')
plt.title('Scatter plot graph')


# In[192]:


plt.scatter(table['Open'], table['Close'])
plt.plot(table['Open'], table['Open'], color='red', label='Title')
plt.title('Scatter plot graph with trend line')


# In[193]:


plt.scatter(table['High'], table['Low'],c=table['High'],cmap=plt.cm.plasma)
plt.title('Scatter plot graph with colormap')
plt.savefig('Newscatter')


# In[170]:


plt.savefig('Newscatter')

