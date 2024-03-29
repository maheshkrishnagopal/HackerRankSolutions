# https://www.hackerrank.com/challenges/chocolate-feast

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    total = 0
    total = int(n / c)
    curr = total 
    while curr >= m:
        wrappers = int(curr / m)
        total = total + wrappers
        curr = wrappers + (curr % m)
    return total
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        ncm = input().split()
        n = int(ncm[0])
        c = int(ncm[1])
        m = int(ncm[2])
        result = chocolateFeast(n, c, m)
        fptr.write(str(result) + '\n')
    fptr.close()
