#!/bin/python3

import sys
from math import sqrt
from operator import mod
def test(x):
    for i0 in range(2, int(sqrt(x)+1)):
        if mod(x,i0)==0:
            return 0
            break
    return 1   
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) 
    j = int(sqrt(n))   
    for i in range(n,1,-1):
        if test(i) and mod(n,i)==0:
            print(i)
            break
