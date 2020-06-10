#Uses python3

import sys
# import pprint

def lcs3(a, b, c):

    #write your code here
    sizea = len(a) # length (col)
    sizeb = len(b) # breadth (row)
    sizec = len(c) # height (h)
    dp = [[[0] * (sizea + 1) for _ in range(sizeb + 1)] for _ in range(sizec + 1)]

    for h in range(1, sizec + 1):
        for row in range(1, sizeb + 1):
            for col in range(1, sizea + 1):
                if b[row -1] == a[col - 1] == c[h - 1]:
                    dp[h][row][col] = dp[h-1][row-1][col-1] + 1
                else:
                    dp[h][row][col] = max(dp[h-1][row][col], dp[h][row-1][col], dp[h][row][col-1])
    # pprint.pprint(dp)
    return dp[sizec][sizeb][sizea]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
# data = list(map(int, "5 8 3 2 1 7 7 8 2 1 3 8 10 7 6 6 8 3 1 4 7".split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
