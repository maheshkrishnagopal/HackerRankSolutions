# https://www.hackerrank.com/challenges/find-digits

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    cnt = 0
    for i in str(n):
        if i == '0':
            continue
        if n%int(i) == 0:
            cnt += 1
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = findDigits(n)
        fptr.write(str(result) + '\n')
    fptr.close()
