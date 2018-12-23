#!/usr/bin/env python3 
#-*- coding: utf-8 -*-
###
# Name: Enea Dodi 
# Student ID: 2296306 
# Email: dodi@chapman.edu 
# Course: PHYS220/MATH220/CPSC220 Fall 2018 Assignment: CW03
###
def main(local_argv):
    from primesE import eratosthenes as eratos
    from primesE import gen_eratosthenes as gen_eratos
    # storing first value in list of command line arguments for use in sequence
    # catching index error in case of no command line option
    try:
        n = int(local_argv[1])
    except IndexError:
        n = 1
    print(eratos(n))
    g = gen_eratos()
    for i in range(20):
        print(next(g))
    
   
    
# Below is the python convention for defining an executable main section
if __name__ == "__main__":
    from primesE import eratosthenes as eratos
    import sys
    main(sys.argv)