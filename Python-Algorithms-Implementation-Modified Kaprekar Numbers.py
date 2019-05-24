# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    result = []
    for num in range(p,q+1):
        num_len = len(str(num))
        sq = num ** 2
        if len(str(sq)) > 1:
            r = int(str(sq)[-(num_len):])
            l = int(str(sq)[:-(num_len)])
            if (r+l) == num:
                result.append(num)
        elif num == sq:
            result.append(num)
    if len(result) == 0:
        print('INVALID RANGE')
    else:
        print(*result)


if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)
