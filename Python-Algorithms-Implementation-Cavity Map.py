# https://www.hackerrank.com/challenges/cavity-map


import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    r = len(grid)
    c = len(grid)
    result = ''
    if r == 2:
        return grid
    for i in range(r):
        for j in range(c):
            if 0 < i <(r-1) and 0< j <(c-1):
                if grid[i-1][j] < grid[i][j] and grid[i+1][j] < grid[i][j] and grid[i][j-1] < grid[i][j] and grid[i][j+1] < grid[i][j]:
                    result += 'X'
                    #print(grid[i][j],'True')
                else:
                    result += grid[i][j]    
            else:
                result += grid[i][j]
        result += ' '
    return result.split()
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
        
    result = cavityMap(grid)
    
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
