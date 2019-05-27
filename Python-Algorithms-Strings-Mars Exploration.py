# https://www.hackerrank.com/challenges/mars-exploration

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    ex = 'SOS'*(int(len(s)/3))
    res = 0
    for i,j in zip(ex,s):
        if i != j:
            res +=1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = marsExploration(s)
    fptr.write(str(result) + '\n')
    fptr.close()
