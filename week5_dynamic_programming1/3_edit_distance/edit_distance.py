# Uses python3
def edit_distance(s, t):
    #write your code here
    size_t = len(t)
    size_s = len(s)
    dp = [[i for i in range(size_t + 1)]] + [[i] + [0] * (size_t) for i in range(1, size_s + 1)]
    for col in range(1, size_t + 1):
        for row in range(1, size_s + 1):
            if s[row - 1] == t[col - 1]:
                dp[row][col] = min(dp[row-1][col] + 1, dp[row][col-1] + 1, dp[row-1][col-1])
            else:
                dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
     
    return dp[size_s][size_t]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
