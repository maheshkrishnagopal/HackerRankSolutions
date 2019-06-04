# https://www.hackerrank.com/challenges/input

x , k = map(int, input().split())
pol = input()
print(True if eval(pol) == k else False)
