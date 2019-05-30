# https://www.hackerrank.com/challenges/np-inner-and-outer

import numpy

A = numpy.array(list(map(int,input().split())))
B = numpy.array(list(map(int,input().split())))
print(numpy.inner(A,B), numpy.outer(A,B), sep="\n")
