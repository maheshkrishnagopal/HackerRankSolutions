# https://www.hackerrank.com/challenges/counting-valleys

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley = 0
    flag = False
    level = 0

    for step in s:
        if step == 'U':
            level += 1
        else:
            level -= 1
        if level < 0 and flag == False:
            flag = True
            valley += 1 
        if level >= 0 and flag == True:
            flag = False
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
