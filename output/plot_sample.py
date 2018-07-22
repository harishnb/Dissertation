# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 12:02:13 2018

@author: harisbha
"""

import pandas as pd
import matplotlib.pyplot as plt
import warnings

data = pd.read_csv('time_spent.csv')
print (data.head())
print (data.describe())
print ("==================")
print (data["Time"].describe())
print (data.dtypes)
print ("========")
data_group = data.groupby('session')
print (data_group.size())

totall = data.sum()
print (totall)
#totall.sort(columns='Time').head()
my_plot = data.plot(kind='bar')
avg_plot = data['Time'].hist(bins=2)
avg_plot.set_title ("avg time")
avg_plot.set_xlabel("Sessionnn")
avg_plot.set_ylabel("Timmme")
