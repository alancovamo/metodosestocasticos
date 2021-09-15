# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 10:32:42 2021

@author: Alan
"""
import numpy as np
import math
import random as rand
import matplotlib.pyplot as plt

#cond iniciales
t0=0
x0=2000
y0=2500

#param

a=0.5
b=1.7
gamma= 1
delta=1
omega=1000
pasos=500000

#edo del sistema
S=np.array([[1,1,-1,-1],
            [0,-1,1,0]])


Y=np.zeros([2,pasos+1])
t=np.zeros(pasos+1)

Y[0][0]=x0
Y[1][0]=y0

def distr_exp(a):
    r=rand.random()
    return -np.log(r)*1/a

def dist_reaccion(ni,A):
    r = rand.random()
    #ciclos para ver si es menor a la propension [i]
    
    
    if (r<ni[0]/A):
        return 0
    elif (r< (ni[0]+ni[1])/A):
        return 1
    elif (r< (ni[0]+ni[1]+ni[2])/A):
        return 2
    elif (r< (ni[0]+ni[1]+ni[2]+ni[3])/A):
        return 3

for i in range(pasos):
    ni = np.array([gamma, a*Y[0][i]*(Y[0][i]-1)*Y[1][i]/omega**3,
                   b*Y[0][i]/omega, delta*Y[0][i]/omega])
    alpha = sum(ni) #suma de propensiones
    tau = distr_exp(alpha) #tiempo en q se va a llevar acabo la sig reaccion
    mu = dist_reaccion(ni,alpha) #cual reaccion se llevara a cabo
    
    
    Y[0][i+1]=Y[0][i]+S[0][mu]
    Y[1][i+1]=Y[1][i]+S[1][mu]
    
    t[i+1] = t[i]+tau
    
plt.plot(Y[0],Y[1])
plt.show()
    
    
    
    

        
    
