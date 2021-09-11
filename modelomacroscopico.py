# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 14:21:16 2021

@author: Alan
"""
from scipy.integrate import odeint
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

y0=np.zeros(2)



def dydt(y,t):
    alpha_1=1
    alpha_2=1
    beta_1=1
    beta_2=1
    
    X_1=y[0]
    X_2=y[1]
    dX_1=alpha_1-beta_1*X_1
    dX_2=alpha_2-beta_2*X_2
    return [dX_1,dX_2]

t=np.linspace(0,10,1000)
X_1=y0[0]=10
X_2=y0[1]=0

y=odeint(dydt,y0,t)


plt.plot(t,y[:])
plt.show()