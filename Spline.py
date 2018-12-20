# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:10:16 2018

@author: Mara
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

helo = pd.read_csv('C:/Users/ivana/Desktop/ETF/3. SEMESTAR/NUMDIS/numdis Mara/exp.csv')

x = helo.x
y = helo.fx

plt.plot(x, y, 'o' )
n = len(x)
X = np.linspace(0, 6, 1000)
s = interpolate.splrep(x, y,k=2) #menjanjem parametra k se bira stepen polinoma
plt.plot(X, interpolate.splev(X, s), label =  'spline')
plt.xlabel('x') 
plt.ylabel('y') 
plt.legend()
plt.show()