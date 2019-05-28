# https://www.hackerrank.com/challenges/itertools-product

from itertools import product

l1 = input().split(" ")
l2 = input().split(" ")
l1 = [int(i) for i in l1]
l2 = [int(i) for i in l2]

for i in product(l1,l2):
    print(i,end=" ")
