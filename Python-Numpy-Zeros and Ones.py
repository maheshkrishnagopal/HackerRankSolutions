# https://www.hackerrank.com/challenges/np-zeros-and-ones

import numpy

x = list(map(int, input().split()))

print(numpy.zeros((x), dtype=numpy.int))
print(numpy.ones((x), dtype=numpy.int))
