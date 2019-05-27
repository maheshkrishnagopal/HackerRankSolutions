# https://www.hackerrank.com/challenges/strong-password

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    lc = False
    uc = False
    ns = False
    sc = False
    if n<6:
        for char in password:
            if char in numbers:
                ns = True
            elif char in lower_case:
                lc = True
            elif char in upper_case:
                uc = True
            elif char in special_characters:
                sc = True
        result = []
        if not(ns):
            result.append(ns)
        if not(lc):
            result.append(lc)
        if not(uc):
            result.append(uc)            
        if not(sc):
            result.append(sc)
        if (6-len(password)) < len(result):
            return len(result)
        else:
            return 6-len(password)
    else:
        for char in password:
            if char in numbers:
                ns = True
            elif char in lower_case:
                lc = True
            elif char in upper_case:
                uc = True
            elif char in special_characters:
                sc = True
        result = []
        if not(ns):
            result.append(ns)
        if not(lc):
            result.append(lc)
        if not(uc):
            result.append(uc)            
        if not(sc):
            result.append(sc)
        return len(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    password = input()
    answer = minimumNumber(n, password)
    fptr.write(str(answer) + '\n')
    fptr.close()
