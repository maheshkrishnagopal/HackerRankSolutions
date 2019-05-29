# https://www.hackerrank.com/challenges/np-concatenate

import numpy

N, M, P = map(int, input().split())
arr1 = list()
for i in range(N):
    arr1.append(list(map(int, input().split())))
arr1 = numpy.array(arr1)
arr2 = list()
for j in range(M):
    arr2.append(list(map(int, input().split())))
arr2 = numpy.array(arr2)
print(numpy.concatenate((arr1,arr2),axis=0))
