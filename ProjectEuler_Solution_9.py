from math import sqrt
k = 1000
for a in range(1, 1000):
        for b in range(1, 1000):
                if 2*a*b == k**2 - 2*k*sqrt(a**2 + b**2):
                        print(a*b*sqrt(a**2 + b**2))
                        break


print("End")

#The problem is https://projecteuler.net/problem=9
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
