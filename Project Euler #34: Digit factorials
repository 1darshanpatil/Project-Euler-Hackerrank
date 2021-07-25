from math import factorial
from operator import mod
c=0
def f(x):
    lst = []
    for i0 in str(x):
        lst.append(factorial(int(i0)))
    return sum(lst)
        
n= int(input())
I=[]
for i in range(10,n):
    if mod(f(i), i)==0:
        c += i
print(c)
