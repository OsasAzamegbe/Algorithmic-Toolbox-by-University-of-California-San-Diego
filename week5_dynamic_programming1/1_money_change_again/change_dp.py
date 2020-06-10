# Uses python3
import sys

def get_change(m):
    #write your code here
    dp = [0]
    denom = {1: 0, 3: 0, 4:0}

    for i in range(1, m + 1):
        for coin in denom:
            if i >= coin:
                if i >= len(dp):
                    dp.append(min(dp[i - 1], dp[i - coin]) + 1)
                else:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
# m = 10000
    print(get_change(m))
