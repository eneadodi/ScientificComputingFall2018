#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sequences

"""sequences.py Test Module

Verifies that the implementations for sequence functions are correct.
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
    
def test_first_five():
    """Verify the first five Fibonacci numbers.
    
    Note that the equality test for the assert here only works because the
    integers inside the list support exact equality. For floating point
    numbers (with decimals), you will need to use the approximate equality
    functions in the nose.tools or numpy.testing modules.
    """
    assert sequences.fibonacci(5) == [1,1,2,3,5]
    
def test_fib_thousand():
    """Verify the thousandth Fibonacci number.
    """
    assert sequences.fibonacci(1000)[-1] == 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
