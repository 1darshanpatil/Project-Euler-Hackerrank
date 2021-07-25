#!/bin/python3

import sys
def f(x):
    ar=[0,1,2]
    if x==1 or x==2:
        return ar[x]
    else:
        for i in range(3,x+1):
            temp = ar[i-1]+ar[i-2]
            ar.append(temp)
    return ar[x]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr=[0]
    s=0
    for i0 in range(1000):
        if arr[i0]>n:
            break
        temp=f(i0)
        arr.append(temp)
        if arr[i0]%2==0:
            s += arr[i0]
    print(s)
