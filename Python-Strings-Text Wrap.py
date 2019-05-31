# https://www.hackerrank.com/challenges/text-wrap


"""
Solution 1
"""

import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    text = wrapper.wrap(string)
    return '\n'.join(text)
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)



"""
Solution 2
"""

import textwrap

def wrap(string, max_width):
    i = 0
    res = list()
    while i <= len(string):
         res.append(string[i:i+max_width])
         i += max_width
    return '\n'.join(res)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
