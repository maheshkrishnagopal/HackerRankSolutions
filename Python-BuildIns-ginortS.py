# https://www.hackerrank.com/challenges/ginorts

string = input()
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(''.join(sorted(string, key=order.index)))
