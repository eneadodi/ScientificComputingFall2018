#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
# Name: Enea Dodi
# Student ID: 2296306
# Email: dodi@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018 Assignment: CW03
###
'''Cw08 module
This module contains the piecewise function and Convergent function
discussed on the cw08 README. The convergent function is said to converge to 
the values produced by the piecewise function '''
import numpy as np

def Sn(t,n):
    '''Sn function
Args: t - a value between -pi/2 and pi/2
      n - amount of recursions of the converging sum function
Returns: the sum of the converging sum function Sn (found on README) 
Should be converting to a value -1,0,or 1 as n grows arbitrary large.'''
    k = np.arange(1,n+1,1)
    constant  = np.divide(4,np.pi)
    
    
    def term(k,t,T = np.multiply(2,np.pi)):
        '''term function
        Args: k - arange of the number of iteratiosn
        t = the Value of a*T
        Returns: The value calcualted at each t which will at the end be summed together.'''
        coefficient = np.divide(1,(2*k-1))
        insideSine = np.divide((2*(2*k-1)*np.pi*t),T)
        return np.multiply(coefficient,np.sin(insideSine))
    
    
    
    vectorizedTerm = np.vectorize(term)
    returnVal = np.multiply(vectorizedTerm(k,t),constant)
    return returnVal.sum()

def f(t):
    '''f function
Args: t - a value between -pi/2 or pi/2
Returns: a value (-1,0, or 1) depending on value of t.'''
    T = np.pi
    if (t < -1*T/2) or (t > T/2):
        raise Exception("t can only be between -T/2 or T/2")
    if t < 0:
        return -1
    elif t > 0:
        return 1
    else:
        return 0