# # Uses python3
# from sys import stdin

# def fibonacci_sum_squares_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current

#     return sum % 10

# if __name__ == '__main__':
#     n = int(stdin.read())
#     print(fibonacci_sum_squares_naive(n))

def fibonacci_sum_squares_last_digit(n):
    # last digits of fibonacci numbers repeat after 60
    n %= 60
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, (a + b) % 10
        
    return ((a + b) * b) % 10

# if __name__ == '__main__':
    # input = sys.stdin.read()
n = int(input())
print(fibonacci_sum_squares_last_digit(n))
