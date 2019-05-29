# https://www.hackerrank.com/challenges/np-arrays

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr, float)
    return numpy.flip(arr)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
