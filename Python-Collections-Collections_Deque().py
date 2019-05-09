# collections.deque()
# A deque is a double-ended queue. It can be used to add or remove elements from both ends.

# Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

# Task

# Perform append, pop, popleft and appendleft methods on an empty deque .

# Input Format

# The first line contains an integer , the number of operations. 
# The next  lines contains the space separated names of methods and their values.

# Constraints

# Output Format

# Print the space separated elements of deque .

# Sample Input
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# Sample Output
# 1 2

"""
----------------------------------------------------------------------------------------------------------------------------------------
"""

from collections import deque
reps = int(input())
res = deque()
for i in range(reps):
    inp = input()
    if ' ' in inp:
        ops, val = inp.split()
    else:
        ops = inp
    if ops == 'append':
        res.append(val)
    elif ops == 'appendleft':
        res.appendleft(val)
    elif ops == 'pop':
        res.pop()
    elif ops == 'popleft':
        res.popleft()
for i in res:
    print(i,end=' ')
