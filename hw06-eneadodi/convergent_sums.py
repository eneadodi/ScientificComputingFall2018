#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''This module contains the functions sum_1, sum_2 and sum_3, which all utilizes the inner functions firstsum(k), secondsum(k) and thirdsum(k).
    Each of the functions compute an "infinite" sum
primes up to the value of positive integer input n'''
###
# Name: Enea Dodi
# Student ID: 2296306
# Email: dodi@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018 Assignment: HW03
###
import math
import numpy as np
import matplotlib.pyplot as plt
def sum_1(tol=1e-5):
    k = 1
    '''sum_1 function
    args: tol, a keyword parameter specifying the default keyword parameter tol representing a tolerance. 
          Stops summation when the next term of the sum would be smaller than this tolerance
    returns: the summation right before the next sum equals the tolerance'''
    def fSum(n):
        '''
        The bread and butter of sum_1. Follows the equation presented by the HW README:
        4\sum_{k=1}^\infty \frac{(-1)^{k+1}}{2k - 1
        args: k, the integer the summation follows.
        returns k put into the equation 4\sum_{k=1}^\infty \frac{(-1)^{k+1}}{2k - 1'''
        return ((-1)**(n+1))/(2*n-1)
    val = fSum(k)
    k += 1
    a = fSum(k)
    val = val + a
    k += 1
    a = fSum(k)
    while(abs(a/val) > tol):
        val = val + a
        k += 1
        a = fSum(k)
    return(4*val)

def sum_2(tol=1e-5):
    k = 0
    '''sum_2 function
    args: tol, a keyword paramete specifying the default keyword parameter tol representing a tolerance. 
          Stops summation when the next term of the sum would be smaller than this tolerance
    returns: the summation right before the next sum equals the tolerance'''
    def sSum(n):
        '''
        The bread and butter of sum_2. Follows the equation presented by the HW README:
        \frac{6}{\sqrt{3}}\sum_{k=1}^\infty \frac{(-1)^{k+1}}{3^k(2k + 1)}
        args: k, the integer the summation follows.
        returns k put into the equation \frac{6}{\sqrt{3}}\sum_{k=1}^\infty \frac{(-1)^{k+1}}{3^k(2k + 1)}'''
        return ((-1)**(n+1))/((3**n)*((2*n)+1))
    val = sSum(k)
    k += 1
    a = sSum(k)
    val = val + a
    k += 1
    a = sSum(k)
    while(abs(a/val) > tol):
        val = val + a
        k += 1
        a = sSum(k)
    return((6/math.sqrt(3))*val*-1)

def sum_3(tol=1e-5):
    k = 0
    '''sum_3 function
    args: tol, a keyword paramete specifying the default keyword parameter tol representing a tolerance. 
          Stops summation when the next term of the sum would be smaller than this tolerance
    returns: the summation right before the next sum equals the tolerance'''
    def tSum(n):
        '''
        The bread and butter of sum_3. Follows the equation presented by the HW README:
        4\sum_{k=1}^\infty \left[ \frac{4(-1)^{k+1}}{5^{2k+1}(2k + 1)} - \frac{(-1)^{k+1}}{239^{2k+1}(2k + 1)} \right]
        args: k, the integer the summation follows.
        returns k put into the equation 4\sum_{k=1}^\infty \left[ \frac{4(-1)^{k+1}}{5^{2k+1}(2k + 1)} - \frac{(-1)^{k+1}}{239^{2k+1}(2k + 1)} \right]'''
        return ((((4*((-1)**(n))))/((5**((2*n)+1))*((2*n)+1)))-(((-1)**(n))/((239**((2*n)+1))*((2*n)+1))))
    val = tSum(k)
    k += 1
    a = tSum(k)
    val = val + a
    k += 1
    a = tSum(k)
    while(abs(a/val) > tol):
        val = val + a
        k += 1
        a = tSum(k)
        
    return(4*val)

def term_1(k):
    return 4*((-1)**(k+1))/(2*k-1)
def term_2(k):
    return ((6/math.sqrt(3))*(((-1)**(k+1))/((3**k)*((2*k)+1)))*-1)
def term_3(k):
    return 4*((((4*((-1)**(k))))/((5**((2*k)+1))*((2*k)+1)))-(((-1)**(k))/((239**((2*k)+1))*((2*k)+1))))

class ConvergentSum(object):

    def __init__(self, f, start=0, tolerance = 1e-5):
        self.term = f
        self.tolerance = tolerance
        self.start = start
        self.partials =[]
        self.value = None
    
    def evaluate(self):
        k = self.start
        val = self.term(k)
        a = val
        while(abs(a/val) > self.tolerance):
            self.partials.append(val)
            k += 1
            a = self.term(k)
            val = val + a
            
        self.value = val
    
    def plot(self):
        if not self.value:
            self.evaluate()
        f = plt.figure(figsize=(8,6))
        a = plt.axes()
        a.set(ylim=(0, 4))
        a.plot(self.partials[:100], color = 'green', label='Convergent Sum', linewidth =2, markersize =10)
        a.set(title="Converging to pi")
        a.plot(np.pi*np.ones_like(self.partials[:100]), color = 'blue', linestyle = '--')
        a.legend()
        a.grid(True)
        plt.show()
        
    def __call__(self):
        if not self.value:
            self.evaluate()
        print(self.value)