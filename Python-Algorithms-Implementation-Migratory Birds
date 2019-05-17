# https://www.hackerrank.com/challenges/migratory-birds

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    max_cnt = 0
    val = 0
    for i in set(arr):
        if arr.count(i) > max_cnt:
            max_cnt = arr.count(i)
            val = i
    return val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
    
