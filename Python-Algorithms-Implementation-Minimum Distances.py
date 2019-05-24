# https://www.hackerrank.com/challenges/minimum-distances

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    dup = set([i for i in a if a.count(i)>1])
    result = []
    temp = 0
    for num in dup:
        for i in enumerate(a):
            if num == i[1]:
                temp = abs(temp - i[0])
        result.append(temp)
        temp = 0
    return min(result) if len(result) >= 1 else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)
    fptr.write(str(result) + '\n')
    fptr.close()
