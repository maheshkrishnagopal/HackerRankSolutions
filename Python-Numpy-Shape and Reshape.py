# https://www.hackerrank.com/challenges/np-shape-reshape

import numpy

inp = input().strip().split(' ')
arr = numpy.array(inp, int)
arr.shape = (3,3)
print(arr)
