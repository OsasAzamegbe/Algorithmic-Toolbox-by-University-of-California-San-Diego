# Uses python3
# import sys

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current

#     return sum % 10


def fibonacci_sum_last_digit(n):
    # last digits of fibonacci numbers repeat after 60
    n %= 60
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, (a + b + 1) % 10
        
    return b

# if __name__ == '__main__':
    # input = sys.stdin.read()
n = int(input())
print(fibonacci_sum_last_digit(n))

