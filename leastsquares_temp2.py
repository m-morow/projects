#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:56:00 2022

@author: mtan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import scipy
from scipy.optimize import minimize
plt.style.use('default')
rcParams['figure.dpi'] = 150

#Data source https://academic.udayton.edu/kissock/http/Weather/citylistUS.htm
df = pd.read_csv("./MIDETROI.txt", delim_whitespace=True, header=None)  
df.head()
df.columns = [['Month','day','year','Temp']]
df.head()
df['k'] = np.arange(len(df)) #need to add append k variable to data
data = np.array(df)

#Set variables----------------------------------
k = data[:,4]
T = data[:,3]

xs = k
ys = T

#Least squares fitting--------------------------
#"Without" climate change
def func(x, A, B, C):
    return  A + B*np.cos(x*2*np.pi/365.25)  + C*np.sin(x*2*np.pi/365.25)

popt, pcov = scipy.optimize.curve_fit(func, xs, ys)

#"With" climate change
def func_climate_change(x, A, B, C, D):
    return A + B*np.cos(x*2*np.pi/365.25)  + C*np.sin(x*2*np.pi/365.25) + D*x*x

popt2, pcov2 = scipy.optimize.curve_fit(func_climate_change, xs, ys)

#Alternative least squares fitting using matrices general form (needs tweaking)
'''
Ycos  = np.cos((np.pi/6)*ys)
Ysin  = np.sin((np.pi/6)*ys)

ycos = np.vstack((np.repeat(1,len(Ycos)),Ycos))
reshape_var = xs.max()
x0 = np.concatenate([ycos,Ysin.reshape(1,reshape_var)]) 
xTx = np.matmul(x0,x0.ys)
xTy = np.matmul(x0,ys)

xTx_inv = np.linalg.inv(xTx)
betas = np.matmul(xTx_inv, xTy)
T0 = betas[0]
beta1 = betas[1]
beta2 = betas[2]

plt.plot(T0 + (beta1*Ycos) + (beta2*Ysin),c='r')
'''

#Generate values for least squares plot---------
x_max = xs.max()
xx = np.linspace(0, x_max, 1000)


#Plotting---------------------------------------
plt.plot(xs, ys, label='data')
plt.plot(xx, (func(xx,*popt)), c='k', ls='--', label='fit')
plt.plot(xx, popt2[0]+xx*popt2[3], c='r', ls='--', alpha=0.5, label='fit2')
plt.xlabel('Date')
plt.xticks(np.arange(0, x_max, step=1825),['1995','2000','2005','2010','2015','2020'])
plt.ylabel('Temperature (F)')
plt.title('Detroit 1995-2020 temperature data least squares regression')
plt.legend()
plt.show()

#Get max and min days of year-------------------
def get_day(x): 
    return func(x, popt[0], popt[1],  popt[2])

max_x = scipy.optimize.fmin(lambda x: -get_day(x), 0)
warmest_day = scipy.optimize.minimize_scalar(lambda x: -get_day(x), bounds=[0,365], method='bounded')
coldest_day = scipy.optimize.minimize_scalar(lambda x: get_day(x), bounds=[0,365], method='bounded')

print('Warmest day:', warmest_day.x)
print('Coldest day:', coldest_day.x)
print('With climate change model, temperatures increase', popt2[3]*365, 'F per year')


