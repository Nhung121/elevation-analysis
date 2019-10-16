#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
import pandas as pd
# elevation = pd.read_excel(r"D:/Nhung/Data/SLAMM/SLAMM_outputs/NormalDEM/NWI/Elevation_Analysis2.xlsx")
elevation = pd.read_excel('./Elevation_Analysis2.xlsx')
# print (elevation)


# In[14]:

# optional: use ggplot style
plt.style.use('ggplot') 

# create plot
fig = elevation.boxplot(figsize=(20, 8), rot=20).get_figure()

# save plot to pdf
fig.savefig('box_plot.pdf')
