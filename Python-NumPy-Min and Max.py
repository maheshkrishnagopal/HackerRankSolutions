# https://www.hackerrank.com/challenges/np-min-and-max

import numpy

N, M = map(int, input().split())
arr = list()
for _ in range(N):
    arr.append(list(map(int,input().split())))
arr = numpy.array(arr)
print(numpy.max(numpy.min(arr,axis=1)))
