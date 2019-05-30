# https://www.hackerrank.com/challenges/np-sum-and-prod

import numpy

N, M = map(int, input().split())
arr = list()
for _ in range(N):
    arr.append(list(map(int,input().split())))
arr = numpy.array(arr)
print(numpy.prod(numpy.sum(arr, axis=0)))
