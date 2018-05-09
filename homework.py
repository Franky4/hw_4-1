
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


DATA_PATH = f'{os.getcwd()}/names/'


# In[106]:


def count_top3(years):
    names_row = ['Name', 'Gender', 'Count']
    names_list = [pd.read_csv(DATA_PATH + 'yob' + str(year) + '.txt', names=names_row) for year in years]
    names_all = pd.concat(names_list)
    names_all2 = names_all.groupby(['Gender', 'Name']).sum()
    names_all2 = names_all2.sort_values(by='Count', ascending=False).head(3)
    print(names_all2.values['Name'])

    return names_all2


def count_dynamics(years):
    names_row = ['Name', 'Gender', 'Count']
    names_list = [pd.read_csv(DATA_PATH + 'yob' + str(year) + '.txt', names=names_row) for year in years]
    names_all = pd.concat(names_list)
    names_all2 = names_all.groupby(['Gender']).sum()
    names_all2 = names_all2.sort_values(by='Count', ascending=False)

    return names_all2

# In[101]:


print(count_top3([1900, 1950, 2000]))

print(count_dynamics([1900, 1950, 2000]))