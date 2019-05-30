# https://www.hackerrank.com/challenges/np-polynomials

import numpy

val = list(map(float, input().split()))
x = int(input())
print(numpy.polyval(val,x))
