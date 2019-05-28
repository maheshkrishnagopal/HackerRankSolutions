# https://www.hackerrank.com/challenges/collections-counter

from collections import Counter

no_of_shoes = int(input())
sizes = Counter([int(i) for i in input().split(" ")])
N = int(input())
sum = 0

for i in range(1,N+1):
    req = [int(i) for i in input().split(" ")]
    if req[0] in sizes and sizes[req[0]] > 0:
        sum += req[1]
        sizes[req[0]] -= 1

print(sum)
