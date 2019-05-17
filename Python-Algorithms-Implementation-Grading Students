# https://www.hackerrank.com/challenges/grading

#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    result = []
    for value in grades:
        nex_mul = value
        if value < 38:
            result.append(value)
        else:
            while nex_mul%5 != 0:
                nex_mul+=1
            if (nex_mul - value) < 3:
                result.append(nex_mul)
            elif  (nex_mul - value) == 3:
                result.append(value)
            else:
                result.append(value)
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
