#Uses python3

import sys

def frac(i):
    divisor = 9
    while divisor < i:
        divisor = 10 * divisor + 9
    return i / divisor

def largest_number(a):
    #write your code here
    a = list(map(int, a))
    a.sort(key=frac, reverse=True)
    a = list(map(str, a))
    return ''.join(a)
   

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
# data = '3 23 39 92'.split()
    a = data[1:]
    print(largest_number(a))

