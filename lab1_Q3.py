# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:51:29 2020

@author: micha
"""

import numpy as np
from time import time
import matplotlib.pyplot as plt


N = np.arange(2,200,20)
time_list = []
for num in N:
    start = time()
    A = np.ones([num,num], float)*3
    B = np.ones([num,num], float)*3
    C = np.ones([num,num], float)*0
#start timer

#iterating through column of A
    for i in range(len(A)):
    #iterating through column of B
        for j in range(len(B)):
        #interating through row of A
            for k in range(len(A[0])):
                C[i][j] += A[i][k]* B[k][j]

#end timer 
    end = time()

#difference is the time used for the calculation
    diff = end - start


    time_list.append(diff)
    

#plotting time vs. N
plt.figure()
plt.title("time vs. Matrix Dimension graph")
plt.xlabel("Dimension of the matrix (N)")
plt.ylabel("Time (years)")
plt.plot(N, time_list, label = "y-variable N")




plt.figure()
plt.title("time vs. Matrix Dimension^3 graph")
plt.xlabel("Dimension of the matrix cubed(N^3)")
plt.ylabel("Time (years)")
plt.plot(N**3, time_list, label = "x-variable N^3 ")


#calculating using np.dot(A,B)
time_list2 = []
for num in N:
    start = time()
    A = np.ones([num,num], float)*3
    B = np.ones([num,num], float)*3
    C = np.dot(A,B)
    end = time()
    diff = end - start
    time_list2.append(diff)

print(time_list) 
print(time_list2) 
    