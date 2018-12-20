# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:22:18 2018

@author: Mara
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


helo = pd.read_csv('C:/Users/ivana/Desktop/ETF/3. SEMESTAR/NUMDIS/numdis Mara/exp.csv')

x = helo.x
y = helo.fx

plt.plot(x, y, 'o' )
n = len(x)
p = np.polyfit(x, y, 3) #menjanjem poslednjeg parametra se bira stepen polinoma
X = np.linspace(0, 6, 1000)
plt.plot(X, np.polyval(p, X), label = 'polyfit')
plt.xlabel('x') 
plt.ylabel('y') 
plt.legend()
plt.show()
