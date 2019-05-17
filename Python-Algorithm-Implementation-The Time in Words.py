# https://www.hackerrank.com/challenges/the-time-in-words

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    if m == 00:
        return (number(h) +' o\' '+'clock' )
    elif 1 <= m <= 30:
        if m == 15:
            return ('quarter past '+ number(h))
        elif m == 30:
            return ('half past '+ number(h))
        else:
            return (number(m) + ' minutes past '+number(h)) if m > 1 else (number(m) + ' minute past '+number(h))
    elif m >= 31:
        if m == 45:
            return ('quarter to '+ number(h+1))
        else:
            return (number(60 - m) + ' minutes to '+ number(h+1))

def number(n):
    
    num2words = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fiveteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
    num2words1 =['twenty','thirty','forty','fivety','sixty','seventy','eighty','ninety']

    if 1 <= n <= 19:
        return num2words[n]
    elif 20 <= n < 99:
        tens, below_ten = divmod(n,10)
        return num2words1[tens - 2] + ' ' + num2words[below_ten]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
