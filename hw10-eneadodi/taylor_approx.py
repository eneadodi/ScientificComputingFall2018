#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Enea Dodi
# Student ID: 2296306
# Email: dodi@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: hw10
###
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
'''taylor_approx module.
Makes taylor approximates of the next value int the series 
knowing the derivatives and their values at a
'''
def derivative(f,x,a,n):
    '''derivative function
    Args: f - the original function
          x - the algebraic symbol in the function f
          a - an x value which we will Taylor-expand around
          n - the amount of derivatives to be calculated
    Returns:
        a numpy array of derivatives of point a
    '''
    fderivs = np.empty(n+1)
    fderivs[0] = (f.replace(x,a))
    nextOrderApproximation = f
    for i in range(len(fderivs)):
        fderivs[i]=(f.replace(x,a))
        f = f.diff(x)
    rfderivs = np.array(fderivs)
    return rfderivs

def taylor(xnum,a,dfs):
    '''taylor function
    Args: xnum - an array of x values (domain)
          a - the x value which we will Taylor-expand around
          dfs - a numpy array of derivatives of point a
     Returns: a numpy array of the same size as xnum which 
     holds the taylor-expanded approximations of the range.'''
    taylorExpansion = np.ones_like(xnum)
    n = dfs.size
    for i in range(len(xnum)):
        rOrderApproximation = 0
        j = 0
        for a in dfs:
            if j == 0:
                rOrderApproximation += a 
            else:
                rOrderApproximation += np.divide(((xnum[i]-a)**j), sp.factorial(j))*a
            j = j + 1
        taylorExpansion[i] = rOrderApproximation
    return taylorExpansion

def plot(taylorExpan,xnum,aVal,n,name):
    '''plot function
    Args: taylorExan -> the taylor values calculated by the taylor method
          xnum - the domain
          title -> what the title of the graph should be
    '''
    s = plt.figure(figsize=(8,6))
    a = plt.axes()
    a.plot(xnum,taylorExpan, color = "blue")
    a.plot(aVal, color ="red")
    a.set_xlabel("x values")
    a.set_ylabel("y values")
    a.set_title(name + " a = " + str(aVal) + " n = " + str(n))
    plt.show()