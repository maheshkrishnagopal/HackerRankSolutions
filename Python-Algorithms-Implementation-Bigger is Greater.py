# https://www.hackerrank.com/challenges/bigger-is-greater


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
        k = None
        # Algorithm used - Generation in lexicographic order.
        """ 
        Finding the largest index k, such that, w[k] < w[k+1]. If no such index exist, w is the last permutation,
        hence, return 'no answer'.
        """

        for i in range(len(w)-1):
            if w[i] < w[i+1]:
                k = i
        if k is None:
            return 'no answer'
        """
        Find the largest index l, greater than k, such that a[k] < a[l].
        """
        l = None
        for j in range(k+1,len(w)):
                if w[k] < w[j]:
                    l = j
        # If no such index exists, return the reversed string w.
        if l == None:
            return w[::-1]

        """
        Swap the values of w[k] and w[l]
        """    
        new_list = list(w)
        new_list[k], new_list[l] = new_list[l], new_list[k]

        """
        Reverse the sequence from w[k+1], upto and including the final element w[n].
        """
        one = new_list[:k+1]
        two = new_list[k+1:][::-1]
        return ''.join(one+two)

      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input())
    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        fptr.write(result + '\n')
    fptr.close()
