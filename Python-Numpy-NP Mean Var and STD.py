# https://www.hackerrank.com/challenges/np-mean-var-and-std

import numpy

if __name__ == "__main__":
    numpy.set_printoptions(legacy='1.13')
    N, M = map(int, input().split())
    val = list()
    for i in range(N):
        val.append(list(map(int, input().split())))
    
    arr = numpy.array(val)
    print(numpy.mean(arr, axis=1))
    print(numpy.var(arr, axis=0))
    #print("{0:.11f}".format(numpy.std(arr, axis=None)))
    print(numpy.around(numpy.std(arr),12))
