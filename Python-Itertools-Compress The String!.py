# https://www.hackerrank.com/challenges/compress-the-string


from itertools import groupby
inp = input()
for k, g in groupby(inp):
        print((len(list(g)), int(k)), end=' ')
