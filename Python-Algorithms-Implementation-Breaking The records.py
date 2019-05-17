# https://www.hackerrank.com/challenges/breaking-best-and-worst-records

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high_score = scores[0]
    high_cnt = 0
    low_score = scores[0]
    low_cnt = 0
    for val in scores[1:]:
        if val > high_score:
            high_score = val
            high_cnt += 1
        elif val < low_score:
            low_score = val
            low_cnt += 1
        else:
            pass
    return [high_cnt,low_cnt]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
