# https://www.hackerrank.com/challenges/np-transpose-and-flatten

import numpy

N, M = map(int, input().split())
inp = list()
for i in range(N):
    t = list(map(int, input().split()))
    inp.append(t)
arr = numpy.array(inp)
print(numpy.transpose(arr))
print(arr.flatten())
