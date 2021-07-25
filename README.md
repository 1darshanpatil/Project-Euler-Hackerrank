# ProjectEuler
ProjectEuler#46
from math import sqrt
from operator import mod
def sq(x):
    q=[]
    for i in range(1,int(sqrt(x))):
        q.append(i**2)
    return q
def p(x):
    if x ==1:
        return 0
    if x in [2,3,5]:
        return 1
    SQ = int(sqrt(x))
    for i in range(2, SQ+1):
        if mod(x, i)==0:
            return 0
    return 1
T= int(input())
for i in range(T):
    N=int(input().strip())
    count = 0
    for u in range(N):
        if p(u):
            for v in sq(N):
                if u+2*v==N:
                    count += 1
    print(count)
