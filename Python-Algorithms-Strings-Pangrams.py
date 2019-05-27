# https://www.hackerrank.com/challenges/pangrams


import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    s = set(s.lower())
    result = 0
    for i in s:
        if ord(i) in range(ord('a'),ord('z')+1):
            result += 1
    # result += 1 for i in s if ord(i) in range(ord('a'),ord('z')+1)
    return 'pangram' if result == 26 else 'not pangram'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = pangrams(s)
    fptr.write(result + '\n')
    fptr.close()
