# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    if n <= 2:
        return [n]
    check = {}
    i = 1
    while True:
        if n//i <= 1:
            summands.append(n)
            return summands
        if i not in check and i * 2 != n:
            n -= i
            summands.append(i)
            check[i] = 0
        i += 1       

    

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
# n = 1000000
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

