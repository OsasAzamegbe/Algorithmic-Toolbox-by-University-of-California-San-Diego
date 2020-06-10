#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    size_a = len(a)     # col
    size_b = len(b)     # row
    dp = [[0] * (size_a + 1) for i in range(size_b + 1)]
    for row in range(1, size_b + 1):
        for col in range(1, size_a + 1):            
            if a[col - 1] == b[row - 1]:
                dp[row][col] = dp[row-1][col-1] + 1
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])

    return dp[size_b][size_a]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
# data = list(map(int, '5 2 0 8 7 3 4 5 2 7 8'.split()))
    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    # a = "A C B A D".split()
    # b = "A B C D".split()
    print(lcs2(a, b))
