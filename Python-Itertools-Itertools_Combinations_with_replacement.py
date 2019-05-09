# itertools.combinations_with_replacement(iterable, r) 
# This tool returns  length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

# Task

# You are given a string . 
# Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.

# Input Format

# A single line containing the string  and integer value  separated by a space.

# Constraints

# The string contains only UPPERCASE characters.

# Output Format

# Print the combinations with their replacements of string  on separate lines.

# Sample Input

# HACK 2
# Sample Output

# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK

"""
-----------------------------------------------------------------------------------------------------------
"""

from itertools import combinations_with_replacement
string, num = input().split()
for i in combinations_with_replacement(sorted(string),int(num)):
    print(''.join(i))
