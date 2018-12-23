#1/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Enea Dodi
# Student ID: 2296306
# Email: dodi@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW03
###

"""This is an executable python script that uses the fibonacci() method form sequencesEnea, reads
one command line argument, and returns the last number added to the array by fibonacci().
"""

def main(local_argv):

    from sequencesEnea import fibonacci as fib
    try:
        n = int(local_argv[1])
    except IndexError:
        n = 1
    print(fib(n).pop())
    
if __name__ == "__main__":
    from sequencesEnea import fibonacci as fib
    import sys
    main(sys.argv)