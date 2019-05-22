# https://www.hackerrank.com/challenges/cut-the-sticks

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    result = []
    cuts = 0
    totalCutLength = 0
    stickLengths = sorted(arr)
    i = 0
    while i < len(stickLengths):
        result.append(len(stickLengths)-i)
        totalCutLength = stickLengths[i]
        while i < len(stickLengths) and stickLengths[i] <= totalCutLength:
            i += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
