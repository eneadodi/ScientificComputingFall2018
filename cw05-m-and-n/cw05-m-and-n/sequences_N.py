#!/usr/bin/env python3
 #-*- coding: utf-8 -*-


def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print (b);
        c=a+b
        a=b
        b=c
