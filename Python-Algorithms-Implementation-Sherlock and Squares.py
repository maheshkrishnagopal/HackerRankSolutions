# https://www.hackerrank.com/challenges/sherlock-and-squares

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    A = int(a**0.5)
    B = int(b**0.5)
    ans = B - A
    if A**2 == a:
        ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        ab = input().split()
        a = int(ab[0])
        b = int(ab[1])
        result = squares(a, b)
        fptr.write(str(result) + '\n')
    fptr.close()
