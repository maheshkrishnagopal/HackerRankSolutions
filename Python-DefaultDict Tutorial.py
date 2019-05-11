# https://www.hackerrank.com/challenges/defaultdict-tutorial


from collections import defaultdict
n, m = map(int, input().split())
DD = defaultdict(list)
for i in range(n):
        val = input()
        DD[val].append(i+1)
for j in range(m):
        val = input()
        if val in DD:
                print(' '.join(map(str,DD[val])))
        else:
                print('-1')
