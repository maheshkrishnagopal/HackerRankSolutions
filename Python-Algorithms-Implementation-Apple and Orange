# https://www.hackerrank.com/challenges/apple-and-orange

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    start = s
    end = t
    apple_tree = a
    orange_tree = b
    d1 = s - a
    d2 = b - t
    app_count = 0
    ora_count = 0
    for val in apples:
        if val > 0 and (val+a) >= start and (val+a) <= end:
            app_count += 1
    for val in oranges:
        if val < 0 and (val+b) >= start and (val+b) <= end:
            ora_count += 1
    print(app_count)
    print(ora_count)
    

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
