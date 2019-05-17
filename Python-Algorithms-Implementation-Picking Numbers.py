# https://www.hackerrank.com/challenges/picking-numbers

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    ans = 0
    a.sort()
    for i in range(len(a)):
        for j in range(len(a)):
            if abs(a[j] - a[i]) <= 1:
                ans = max(ans, j-i+1)
    
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    fptr.write(str(result) + '\n')
    fptr.close()
