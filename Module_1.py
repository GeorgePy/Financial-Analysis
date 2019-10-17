#!/usr/bin/env python
# coding: utf-8

# # Import data
# In this Jupyter Notebook, you will learn how to import data from CSV into Jupyter Notebook

# In[ ]:


# Import data
In this Jupyter Notebook, you will learn how to import data from CSV into Jupyter Notebook# Import data
In this Jupyter Notebook, you will learn how to import data from CSV into Jupyter Notebook


# In[ ]:


#import the package "Pandas" into Jupyter Notebook
import pandas as pd


# In[2]:


#We import the stock data of Facebook into Jupyter Notebook. The CSV file is located in the folder called "Data" in your Workspace
#We then name the DataFrame name as 'fb'
fb = pd.DataFrame.from_csv('../data/facebook.csv')


# ### Instruction
# Now is your turn to import the stock price of Microsoft (microsoft.csv), of which the CSV is located in the same folder, and rename the Dataframe in "ms". 

# In[ ]:


ms = pd.DataFrame.from_csv('../data/microsoft.csv')


# In[4]:


# run this cell to ensure Microsoft's stock data is imported
print(ms.iloc[0, 0])


# # DataFrame

# In[1]:


#import the packages "Pandas" and "MatPlotLib" into Jupyter Notebook
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#import Facebook's stock data
fb = pd.DataFrame.from_csv('../data/facebook.csv')


# In[4]:


print(fb.head())


# In[5]:


#It is your turn to import Microsoft's stock data - "microsoft.csv", which is located in the same folder of facebook.csv
#Replace "None" with your code
ms = pd.DataFrame.from_csv('../data/microsoft.csv')


# In[6]:


# print head of ms, 1 line
print(ms.head())


# ** Expected Output: **

# <tr>
#     <th>Date</th>
#     <th>Open</th>  
#     <th>High</th>
#     <th>Low</th>
#     <th>Close</th>
#     <th>Adj Close</th>
#     <th>Volume</th>
# </tr>
# <tr>
#     <td>2014-12-31</td>
#     <td>46.730000</td>  
#     <td>47.439999</td>
#     <td>46.450001</td>
#     <td>46.450001</td>
#     <td>42.848763</td>
#     <td>21552500</td>
# </tr>
# <tr>
#     <td>2015-01-02</td>
#     <td>46.660000</td>  
#     <td>47.419998</td>
#     <td>46.540001</td>
#     <td>46.759998</td>
#     <td>43.134731</td>
#     <td>27913900</td>
# </tr>
# <tr>
#     <td>2015-01-05</td>
#     <td>46.369999</td>  
#     <td>46.730000</td>
#     <td>46.250000</td>
#     <td>46.330002</td>
#     <td>42.738068</td>
#     <td>39673900</td>
# </tr>
# <tr>
#     <td>2015-01-06</td>
#     <td>46.380001</td>  
#     <td>46.750000</td>
#     <td>45.540001</td>
#     <td>45.650002</td>
#     <td>42.110783</td>
#     <td>36447900</td>
# </tr>
# <tr>
#     <td>2015-01-07</td>
#     <td>45.980000</td>  
#     <td>46.459999</td>
#     <td>45.490002</td>
#     <td>46.230000</td>
#     <td>42.645817</td>
#     <td>29114100</td>
# </tr>
# 

# ## Show the size of a DataFrame using "Shape"

# In[6]:


print(fb.shape)


# In[8]:


# print the shape of ms, 1 line
print(ms.shape)


# ## Show summary statistics of a DataFrame

# In[8]:


# print summary statistics of Facebook
print(fb.describe())


# In[9]:


# print summary statistics of Microsoft
print(ms.describe())


# ## Locate a particular row of data using "Selection by label"

# In[10]:


# select all the price information of Facebook in 2016.
fb_2015 = fb.loc['2015-01-01':'2015-12-31']


# In[11]:


# print the price of Facebook on '2015-03-16'
print(fb_2015.loc['2015-03-16'])


# In[13]:


# select all the price information of Microsoft in 2016.
ms_2016 = ms.loc['2016-01-01':'2016-12-31']


# In[14]:


# print the price of Microsoft on '2016-03-16'
print(ms_2016.loc['2016-03-16'])


# ## Locate a particular row of data using "Selection by position"

# In[14]:


# print the opening price of the first row
print(fb.iloc[0, 0])


# In[30]:


# print the opening price of the last row
print(ms.iloc[-1,0])


# ## Plot the stock data using plot() method

# In[36]:


plt.figure(figsize=(10, 8))
fb['Close'].plot()
plt.show()


# In[34]:


plt.figure(figsize=(10, 8))
# plot only the Close price of 2016 of Microsoft, 1 line 
ms_2016['Close'].plot()
plt.show()


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


fb = pd.DataFrame.from_csv('../data/facebook.csv')
ms = pd.DataFrame.from_csv('../data/microsoft.csv')


# ## Create a new column in the DataFrame (1) - Price difference

# In[4]:


#Create a new column PriceDiff in the DataFrame fb
fb['PriceDiff'] = fb['Close'].shift(-1) - fb['Close']


# In[6]:


fb.head()


# In[7]:


#Your turn to create PriceDiff in the DataFrame ms
ms['PriceDiff'] = ms['Close'].shift(-1) - ms['Close']


# In[8]:


ms.head()


# In[9]:


#Run this code to display the price difference of Microsoft on 2015-01-05
print(ms['PriceDiff'].loc['2015-01-05'])


# ** Expected Output: ** -0.68

# ## Create a new column in the DataFrame (2) - Daily return
# 
# Daily Return is calcuated as PriceDiff/Close

# In[10]:


#Create a new column Return in the DataFrame fb
fb['Return'] = fb['PriceDiff'] /fb['Close']


# In[11]:


fb.head()


# In[12]:


#Your turn to create a new column Return in the DataFrame MS
ms['Return'] = ms['PriceDiff']/ms['Close']


# In[13]:


ms.head()


# In[14]:


#Run this code to print the return on 2015-01-05
print(ms['Return'].loc['2015-01-05'])


# ## Create a new column in the DataFrame using List Comprehension - Direction

# In[15]:


#Create a new column Direction. 
#The List Comprehension means : if the price difference is larger than 0, denote as 1, otherwise, denote as 0,
#for every record in the DataFrame - fb
fb['Direction'] = [1 if fb['PriceDiff'].loc[ei] > 0 else 0 for ei in fb.index ]


# In[16]:


fb.head()


# In[17]:


# Your turn to create a new column Direction for MS

ms['Direction'] = [1 if ms['PriceDiff'].loc[ei] > 0 else 0 for ei in ms.index ]


# In[19]:


ms.head()


# In[20]:


# Run the following code to show the price difference on 2015-01-05
print('Price difference on {} is {}. direction is {}'.format('2015-01-05', ms['PriceDiff'].loc['2015-01-05'], ms['Direction'].loc['2015-01-05']))


# ## Create a new column in the DataFrame using Rolling Window calculation (.rolling()) - Moving average

# In[ ]:


fb['ma50'] = fb['Close'].rolling(50).mean()

#plot the moving average
plt.figure(figsize=(10, 8))
fb['ma50'].loc['2015-01-01':'2015-12-31'].plot(label='MA50')
fb['Close'].loc['2015-01-01':'2015-12-31'].plot(label='Close')
plt.legend()
plt.show()


# In[21]:


# You can use .rolling() to calculate any numbers of days' Moving Average. This is your turn to calculate "60 days"
# moving average of Microsoft, rename it as "ma60". And follow the codes above in plotting a graph

ms['ma60'] = ms['Close'].rolling(60).mean()

#plot the moving average
plt.figure(figsize=(10, 8))
ms['ma60'].loc['2015-01-01':'2015-12-31'].plot(label='MA60')
ms['Close'].loc['2015-01-01':'2015-12-31'].plot(label='Close')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




