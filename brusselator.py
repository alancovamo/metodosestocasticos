# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:43:01 2021

@author: Alan
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

y0=np.zeros(2)

def dydt(y,t):
    gamma=1
    a=1
    b=2.5
    delta=1
    x1=y[0]
    x2=y[1]
    dx1=gamma+a*x2*x1**2-b*x1-delta*x1
    dx2=-a*x2*x1**2+b*x1
    return [dx1,dx2]

t=np.linspace(0,1000,10000)
x1=y0[0]=1
x2=y0[1]=0

y=odeint(dydt,y0,t)

print(y)
#plt.plot(t,y[:])
plt.figure(1)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.plot(y[:,0],y[:,1])
plt.show()