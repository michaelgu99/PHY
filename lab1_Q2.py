# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 16:21:46 2020

@author: micha
"""
import matplotlib.pyplot as plt
import numpy as np
import MyFunctions as mf
from random import random
from scipy.optimize import curve_fit

"""
#Q2a

Let number of years be p and create array from year 0 to year p
let x be an array with len i in range (0,p) 
where x[i] represent the population of i_th year 

for each i, x_(i+1) = r(1-x_i)x_i.

plot x vs. year array with labeled axis, title...
"""

#Q2c
time = np.arange(0, 51)
plt.figure()
plt.title("x_p vs. time graph")
plt.xlabel("time(years)")
plt.ylabel("x_p")
plt.plot(time,mf.x_p(0.1,2,50), color = "Blue") #x_0 = 0.1 r = 2 p_max = 50
plt.plot(time,mf.x_p(0.1,3.4,50), color = "Violet")#x_0= 0.1 r= 3.4 p_max= 50
plt.plot(time,mf.x_p(0.1,2.4,50), color = "Purple")#x_0= 0.1 r= 2.4 p_max= 50
plt.plot(time,mf.x_p(0.1,2.9,50), color = "Orange")#x_0= 0.1 r= 2.9 p_max= 50
plt.plot(time,mf.x_p(0.1,3,50), color = "Green")#x_0= 0.1 r= 3 p_max= 50

#Q2D

r_array = np.arange(2,4.005,0.005) #creating array of r values from 2 to 4
plt.figure()
for i in r_array:
    if i < 3:      
        x_array = mf.x_p(0.1,i,2000)
        r_value= np.ones(100)*i 
        plt.plot(r_value, x_array[1900:2000], "k.",markersize = 0.1)
    if i >= 3:
        x_array = mf.x_p(0.1,i,2000)
        r_value= np.ones(1000)*i
        plt.plot(r_value, x_array[1000:2000],"k.", markersize = 0.1)

#Q2e
r_array = np.arange(3.738,3.745,0.00001)
plt.figure()
for i in r_array:

    x_array = mf.x_p(0.1,i,2000)
    r_value= np.ones(1000)*i
    plt.plot(r_value, x_array[1000:2000],"k.", markersize = 0.1)
    
    
#Q2f:
randomNum = random()*0.000001 #Generate a random number << x_0
r =4
time = np.arange(0,51) # set time array for plotting
plt.figure()
x_0 = 0.35 #setting value for x_0 to be 0.1
x_array1 = mf.x_p(x_0, r, 50)
x_array2 = mf.x_p(x_0+randomNum, r, 50)
plt.plot(time, x_array1, label = "x_0")
plt.plot(time, x_array2, label = "x_0 +e")
plt.xlabel("Time (year)")
plt.ylabel("x_p Value")
plt.legend(loc = "upper right")

delta = np.abs(x_array2 - x_array1) #set the difference to be delta
plt.figure()
plt.semilogy()
plt.plot(time, delta)

#curve fitting to find lambda 
def delta_func(p,a,b):
    return a*np.exp(b*p)

#since the slope is only from 0 to 20, we only need fit on this part
fit_time = np.arange(0,21)

popt, pcov = curve_fit(delta_func,fit_time,\
                              delta[0:21])
plt.plot(time, delta_func(time,popt[0],popt[1]))

'''
popt[0]
Out[270]: 5.494533276043215e-08

popt[1]
Out[271]: 0.8213500502256239
'''

    

    


