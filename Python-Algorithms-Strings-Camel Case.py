# https://www.hackerrank.com/challenges/camelcase


import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    num = 1
    for letter in s:
        if letter.isupper():
            num += 1
    return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = camelcase(s)
    fptr.write(str(result) + '\n')
    fptr.close()
