# Uses python3
# import random
import sys

def naive(W, w):
    size = len(w)   # row
    dp = [[0]  * (W + 1) for _ in range(size + 1) ]
    for row in range(1, size + 1):
        node = w[row - 1]
        for col in range(1, W + 1):
            if node <= col:
                dp[row][col] = max(dp[row - 1][col], dp[row - 1][col - node] + node)
            else:
                dp[row][col] = dp[row - 1][col]
    return dp[size][W]


# def optimal_weight(W, w):
    # write your code here
    # h = {}
    # n = len(w)
    # def helper(w, n):
    #     if (w, n) in h:
    #         return h[(w, n)]
    #     for i in range(1, n):
    #         if



    # result = 0
    # for x in w:
    #     if result + x <= W:
    #         result = result + x
    # return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(naive(W, w))
# W, n, *w = [19, 4, 8, 16, 20, 5]
# print(naive(W, w))

# count = 0
# while True:
#     W, w = random.randrange(9000, 10001), list(set([random.randrange(50, 100001) for _ in range(random.randrange(250, 301))]))
#     print("w:", w, "W:", W)
#     print("result:", naive(W, w), "\n---------------------------------------------------\n")
#     if count == 0:
#         print("END!")
#         break
#     count += 1
