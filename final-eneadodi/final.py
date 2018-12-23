#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Enea Dodi
# Student ID: 2296306
# Email: dodi@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: Final!
###
'''
This is the Python module for the final project!
the module has a method:
    solve_odes which finds all the
x y and z values knowing their original position and runge kutta to find
the next position.
    7 plotting functions- three time graphs, three 2D graphs, and one 3D graph
to analyze the relationships between the odes.
    scatter which finds the local maxima of the x values and makes a scatterplot of them
    over the rnage of c [2,6]

'''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import numba as nb
from scipy.signal import argrelextrema
from mpl_toolkits.mplot3d import Axes3D

def dydt(x,a,y):
    '''dydt function
Args: x - the value at x(t)
      a - constant.
      y - the value at y(t)
Returns: y'(t)'''
    return np.float64(x+a*y)

def dxdt(y,z):
    '''dxdt function
Args: y - the value at x(t)
      z - the value at z(t)
Returns: x'(t)'''
    return np.float64(-y-z)

def dzdt(b,z,x,c):
    '''dzdt function
Args: x - the value at x(t)
      a - constant.
      y - the value at y(t)
Returns: y'(x)'''
    return b+np.float64(z)*x-z*c

@nb.jit
def dtReturn(t1,t0):
    return t1-t0

@nb.jit
def FourthOrderRungeKuttaY(dt,x,a,y,y0):
    '''FourthOrderRUngeKuttaY function
Args: dt - change of t
      x - The x value at t
      a - constant
      y - the y value at t
      y0 - the inital y (at t-1)'''
    K1y = dt*dydt(x,a,y)
    K2y = dt*(dydt(x,a,y)+K1y/2)
    K3y = dt*(dydt(x,a,y)+K2y/2)
    K4y = dt*(dydt(x,a,y)+K3y)
    return y0+(K1y+2*K2y+2*K3y+K4y)/6

@nb.jit
def FourthOrderRungeKuttaX(dt,y,z,x0):
    '''FourthOrderRUngeKuttaX function
Args: dt - change of t
      y - the y value at t
      z - the z value at t
      x0 - the inital x (at t-1)'''
    K1x = dt*(dxdt(y,z))
    K2x = dt*(dxdt(y,z)+K1x/2)
    K3x = dt*(dxdt(y,z)+K2x/2)
    K4x = dt*(dxdt(y,z)+K3x)
    return x0+(K1x+2*K2x+2*K3x+K4x)/6

@nb.jit
def FourthOrderRungeKuttaZ(dt,b,z,x,c,z0):
    '''FourthOrderRUngeKuttaY function
Args: dt - change of t
      b - constant
      z - the z value at t
      c - the constant
      z0 - the inital z (at t-1)'''
    K1z = dt*(dzdt(b,z,x,c))
    K2z = dt*(dzdt(b,z,x,c)+K1z/2)
    K3z = dt*(dzdt(b,z,x,c)+K2z/2)
    K4z = dt*(dzdt(b,z,x,c)+K3z)
    return z0 + (K1z + 2*K2z + 2*K3z + K4z)/6

@nb.jit
def solve_odes(c, T=500, dt=0.001,a=0.2,b=0.2):
    '''solve_odes function
Args: c - tunable parameter user inputs for eqs (1)
      T - the final time t
      dt - the rate of change of t.
Returns: a pandas datafram of four numpy array of float64 values
        pd.DataFrame("t":t, "x":x, "y":y, "z":z)'''
    t = np.arange(0,T,dt,dtype=np.float64)
    x = np.zeros_like(t, dtype= np.float64)
    y = np.zeros_like(t, dtype= np.float64)
    z = np.zeros_like(t, dtype= np.float64)
    for i in range(1,len(t)):
        y[i] = FourthOrderRungeKuttaY(dt,x[i-1],a,y[i-1],y[i-1])
        x[i] = FourthOrderRungeKuttaX(dt,y[i-1],z[i-1],x[i-1])
        z[i] = FourthOrderRungeKuttaZ(dt,b,z[i-1],x[i-1],c,z[i-1])
    returnDataframe = pd.DataFrame({"t":t,"x":x,"y":y,"z":z})
    return returnDataframe

@nb.jit
def plotAll(sol):
    '''plotAll
Args: sol - the panda dataframe
      N - The amount of points to discard
Returns: Plots All the needed graphs'''
    plotx(sol)
    ploty(sol)
    plotz(sol)
    plotxy(sol)
    plotyz(sol)
    plotxz(sol)
    plotxyz(sol)

@nb.jit
def plotx(sol):
    '''plotx function
Args: sol - the panda dataframe
Returns: Plots x v t'''
    s = plt.figure(figsize=(8,6))
    a = plt.axes()
    a.plot(sol["t"],sol["x"], color = "blue")
    a.set_xlabel("t values")
    a.set_ylabel("x values")
    a.set_title("x vs t")
    plt.show()

@nb.jit
def ploty(sol):
    '''ploty function
Args: sol - the panda dataframe
Returns: Plots y v t'''
    s = plt.figure(figsize=(8,6))
    a = plt.axes()
    a.plot(sol["t"],sol["y"], color = "red")
    a.set_xlabel("t values")
    a.set_ylabel("y values")
    a.set_title("y vs t")
    plt.show()

@nb.jit
def plotz(sol):
    '''plotz function
Args: sol - the panda dataframe
Returns: Plots z v t'''
    s = plt.figure(figsize=(8,6))
    a = plt.axes()
    a.plot(sol["t"],sol["z"], color = "black")
    a.set_xlabel("t values")
    a.set_ylabel("z values")
    a.set_title("z vs t")
    plt.show()


@nb.jit
def plotxy(sol,S=100):
    '''plotxy function
Args: sol - the panda dataframe
Returns: Plots x v y'''
    N = (int)(S/(sol["t"][1]-sol["t"][0]))
    s = plt.figure(figsize=(8,6))
    a = plt.axes()
    xvals = sol["x"]
    yvals = sol["y"]
    a.plot(xvals[N:],yvals[N:], color = "orange")
    a.set_xlabel("x values")
    a.set_ylabel("y values")
    a.set_title("y vs x")
    plt.show()

@nb.jit
def plotyz(sol,S=100):
    '''plotyz
Args: sol - the panda dataframe
Returns: Plots y v z'''
    N = (int)(S/(sol["t"][1]-sol["t"][0]))
    s = plt.figure(figsize=(8,6))
    a = plt.axes()
    yvals = sol["y"]
    zvals = sol["z"]
    a.plot(yvals[N:],zvals[N:], color = "green")
    a.set_xlabel("y values")
    a.set_ylabel("z values")
    a.set_title("z vs y")
    plt.show()

@nb.jit
def plotxz(sol,S=100):
    '''plotxz function
Args: sol - the panda dataframe
Returns: Plots x v z'''
    N = (int)(S/(sol["t"][1]-sol["t"][0]))
    s = plt.figure(figsize=(8,6))
    a = plt.axes()
    xvals = sol["x"]
    zvals = sol["z"]
    a.plot(xvals[N:],zvals[N:], color = "purple")
    a.set_xlabel("x values")
    a.set_ylabel("z values")
    a.set_title("z vs x")
    plt.show()
    
@nb.jit
def plotxyz(sol,S=100):
    '''plotxyz function
Args: sol - the panda dataframe
Returns: Plots x v t v z'''
    fig = plt.figure(1, figsize=(12,8))
    ax = Axes3D(fig)
    N = (int)(S/(sol["t"][1]-sol["t"][0]))
    xvals = sol["x"]
    yvals = sol["y"]
    zvals = sol["z"]
    ax.set_zlim(0, 25)
    ax.set_xlim(-12,12)
    ax.set_ylim(-12,12)
    ax.scatter(xvals[N:],yvals[N:],zvals[N:])
    ax.set_xlabel('x values')
    ax.set_ylabel('y values')
    ax.set_zlabel('z values')
    ax.set_title("z vs x-y")
    plt.show()

@nb.jit
def plotJustTopPeaks(sol):
    '''plotJustTopPeaks method
    Args: sol - The pd dataframe from solve_odes
    plots the alternating peaks at the top of the 
    time graphs as well as overlays them
    '''
    fig = plt.figure(figsize=(8,6))
    
    plt.subplot(2, 2, 1)
    plt.plot(sol["t"],sol["x"], color = "blue")
    
    
    plt.subplot(2, 2, 2)
    plt.plot(sol["t"],sol["y"], color = "blue")
    
    plt.subplot(2, 2, 3)
    plt.plot(sol["t"],sol["z"], color = "blue")

    plt.subplot(2, 2, 4)    
    plt.plot(sol["t"],sol["x"], color = "blue")
    plt.plot(sol["t"],sol["y"], color = "red")
    plt.plot(sol["t"],sol["z"], color = "orange")
    
    plt.gcf().get_axes()[0].set_ylim(4,10)
    plt.gcf().get_axes()[1].set_ylim(2,6)
    plt.show()
    
    
@nb.jit
def findMaxima(x, S=100):
    '''findMaxima function
    Args: x - the X values
          S - For the steady state time domain
    Returns: The local x maxima
    '''
    N = (int)(S/(0.001))
    xPastN = np.array(x[N:])
    xExtrema = argrelextrema(xPastN, np.greater)
    return xPastN[xExtrema]

@nb.jit
def scatter(dc=0.01):
    '''scatter method
    Ards: dt - the change in t
    extrats the set of local maximal points of x , for all c in the 
    range [2,6], then plots each maximal point (c,x) on a scatterplot
    of x vs c. The graph will be a graph of the multi-valued function 
    of the asymptotic local maxima of x.'''
    cVals = np.arange(2,6,dc)
    fig = plt.figure()
    for i in range(0,len(cVals)):
        odes = solve_odes(cVals[i])
        xMaxima = findMaxima(odes["x"])
        currCVal = np.full(len(xMaxima),cVals[i])
        plt.scatter(currCVal,xMaxima, marker='.', color = 'k')
    plt.show()