# https://www.hackerrank.com/challenges/append-and-delete

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):

    #if (len(s)-len(t)) > k:
    #    return 'No'
    #else:
    #    diff = 0
    #    for x,y in zip(s,t):
    #        if x!=y:
    #            diff +=1
    #    if diff >= k:
    #        return 'No'
    #    else:
    #        return 'Yes'

    j = 0
    for i in range(min(len(t),len(s))):
        if s[i] != t[i]:
            break
        else:
            j += 1
    if ((len(s) + len(t)) - 2 * j) > k:
        return 'No'
    if ((len(s) + len(t)) - 2 * j) % 2 == k%2:
        return 'Yes'
    if len(s) + len(t) < k:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    t = input()
    k = int(input())
    result = appendAndDelete(s, t, k)
    fptr.write(result + '\n')
    fptr.close()
