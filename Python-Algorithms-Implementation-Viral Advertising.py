# https://www.hackerrank.com/challenges/strange-advertising

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared = 5
    liked = math.floor(5/2) 
    cum = math.floor(5/2)

    for i in range(n-1):
        shared = liked * 3
        liked = math.floor(shared/2)
        cum += liked
    return cum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()
