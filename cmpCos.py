# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 08:47:56 2018

@author: Mara
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

helo = pd.read_csv('C:/Users/ivana/Desktop/ETF/3. SEMESTAR/NUMDIS/numdis Mara/cosh1.csv')

x = helo.x
y = helo.fx

plt.plot(x, y, 'o')
n = len(x)
p = np.polyfit(x, y, n-1)
X = np.linspace(0, 5800, 10000)
plt.plot(X, np.polyval(p, X), label = 'polyfit')
s = interpolate.splrep(x, y, k=3)
plt.plot(X, interpolate.splev(X, s), label =  'spline')
plt.legend()
plt.show()