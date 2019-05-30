# https://www.hackerrank.com/challenges/np-linear-algebra

import numpy

N = int(input())
numpy.set_printoptions(legacy='1.13')
arr = numpy.array([input().split() for _ in range(N)], float)
print(numpy.linalg.det(arr))
