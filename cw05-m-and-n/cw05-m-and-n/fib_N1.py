#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#a = int(input("amount:"))
def fib_gen():
    
    a = 1
    b = 1
    while True:
 #   for _ in range(n):
        yield b
        a , b = b , a + b

#print(list(fib_gen(a)))


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib4=[]
        f = fib_gen()
        for i in range(0,n):
            fib4.append(next(f))
        return fib4

