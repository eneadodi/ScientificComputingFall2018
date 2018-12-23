#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import taylor_approx as ta
import sympy as sp
import numpy as np

def test_taylor():
    '''Tester function for taylor_approx.
    uses math.isclose to see if the approximation created by the taylor
    method roughly estimates the actually value
    '''
    sp.init_printing()
    x,y = sp.symbols('x y')
    f,g = sp.symbols('f g', cls=sp.Function)
    f = sp.sin(x)
    xVals = np.linspace(-5,5,1000)
    d = ta.derivative(f,x,0,4)
    l = taylor(xVals,0,d):
    assert math.isclose(l[500],sp.sin(0),rel_tol=0.1)