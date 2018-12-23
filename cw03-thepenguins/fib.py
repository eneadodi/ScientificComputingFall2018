#!/usr/bin/env python3 
#-*- coding: utf-8 -*-
###
# Name: Jack Savage 
# Student ID: 2295072 
# Email: jsavage@chapman.edu 
# Course: PHYS220/MATH220/CPSC220 Fall 2018 Assignment: CW03
###
def main(local_argv):
    from sequences import fibonacci as fib
    
    
    # storing first value in list of command line arguments for use in sequence
    # catching index error in case of no command line option
    try:
        n = int(local_argv[1])
    except IndexError:
        n = 1

    print(fib(n).pop())

# Below is the python convention for defining an executable main section
if __name__ == "__main__":
    from sequences import fibonacci as fib
    import sys
    main(sys.argv)
