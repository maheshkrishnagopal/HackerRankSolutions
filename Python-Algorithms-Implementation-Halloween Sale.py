# https://www.hackerrank.com/challenges/halloween-sale/problem

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    cnt = 0
    while s > 0:
        s = s - p
        p = p - d
        if p <= m:
            p = m
        if s < 0:
            break
        cnt += 1
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    pdms = input().split()
    p = int(pdms[0])
    d = int(pdms[1])
    m = int(pdms[2])
    s = int(pdms[3])
    answer = howManyGames(p, d, m, s)
    fptr.write(str(answer) + '\n')
    fptr.close()
