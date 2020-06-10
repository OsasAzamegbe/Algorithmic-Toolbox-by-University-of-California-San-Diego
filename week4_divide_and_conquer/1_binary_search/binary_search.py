# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a) - 1
    # write your code here
    def helper (a, x, left, right):
        if left > right:
            return -1
        mid = left + ((right - left) // 2)
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            return helper(a, x, left, mid - 1)
        else:
            return helper(a, x, mid + 1, right)
    return helper(a, x, left, right)


# def linear_search(a, x):
#     for i in range(len(a)):
#         if a[i] == x:
#             return i
#     return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    # data = list(map(int, '5 1 5 8 12 13 5 8 1 23 1 11'.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
