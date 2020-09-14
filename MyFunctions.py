# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 16:46:01 2020

@author: micha
"""
import numpy

def x_p(x_0, r, p_max):
    ''' Return an array of x_p with equation x_(p+1) = r(1-x_p)x_p.
    Input: 
    x_0[float] is the initial population
    r[float] is the maximum reproduction,
    p_max[float] is the maximum number of years
    Return: 
    x[array] which has p+1 elements which is from year 0 to p_max, is the 
    value x_p we want. '''

    years = numpy.arange(0,p_max+1)
    x = numpy.ones(len(years))
    x[0] = x_0
    for i in range(0,p_max):
        x[i+1] = r*(1-x[i])*x[i]
    return x

    
    