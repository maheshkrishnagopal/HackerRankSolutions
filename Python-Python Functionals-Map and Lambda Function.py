# https://www.hackerrank.com/challenges/map-and-lambda-expression

cube = lambda x: x**3

def fibonacci(n):
    a = 0
    b = 1
    L = []
    if n == 0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        for i in range(n):
            L.append(a)
            c = a+b
            a = b
            b = c
    return L

if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))
