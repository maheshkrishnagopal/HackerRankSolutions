# https://www.hackerrank.com/challenges/itertools-permutations

from itertools import permutations

inp = input().split(" ")
lis = []

for i in permutations(inp[0],int(inp[1])):
    lis.append(''.join(i))

for i in sorted(lis):
    print(i)
