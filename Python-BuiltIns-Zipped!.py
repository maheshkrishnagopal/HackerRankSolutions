# https://www.hackerrank.com/challenges/zipped

N, X = map(int, input().split())
marks = list()
for i in range(X):
    marks.append(list(map(float,input().split())))
avg = list()
for i in range(N):
    val = 0
    for j in marks:
        val += j[i]
    avg.append(val/X)
for row in avg:
    print(row)
