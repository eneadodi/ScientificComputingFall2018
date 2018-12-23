#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import convergent_sums
import math
"""convergent_sums.py Test Module

Verifies that the implementations for convergent_sums functions are correct.
"""

def test_dummy():
    """Dummy test function for nosetests3
    
    Any function name starting with prefix test_ will be automatically run
    by nose. Ideally these should be put in a separate file that also
    begins with the prefix test_.
    
    In a test function, use an assert command to test a Boolean statement
    about how your code executed.  If the assert fails, it throws
    an exception, which is caught by nose and reported as a failure.
    Anything that is printed to the screen during this function is
    suppressed unless there is a failure, where it can be used for
    debugging.
    """
    assert True
    
def test_sum_1():
    """Verify sum_1 outputs the right value.
    """
    assert math.isclose(convergent_sums.sum_1(10),math.pi,rel_tol=0.2, abs_tol=0.0)
    
def test_sum_2():
    """Verify sum_2 outputs the right value
    """
    assert math.isclose(convergent_sums.sum_2(10),math.pi,rel_tol=0.2, abs_tol=0.0)
def test_sum_3():
    """Verify sum_3 outputs the right value
    """
    assert math.isclose(convergent_sums.sum_3(10),math.pi,rel_tol=0.2, abs_tol=0.0)