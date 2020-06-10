# Uses python3
# import sys

# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0

#     current = 0
#     next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             sum += current

#         current, next = next, current + next

#     return sum % 10


# if __name__ == '__main__':
#     input = sys.stdin.read();


def fibonacci_partial_sum(m, n):
    # last digits of fibonacci numbers repeat after 60
    m %= 60
    n %= 60
    if m > n:
        n += 60
    # take care of edge conditions for 0 and 1
    if  n <= 1:
        return n 
      
    if m == 0:
        m = 1

    a, b, = 0, 1

    if m > 1:
        for _ in range(m-1):
            a, b = b, (a + b) % 10
    
    sum = b
    if n == m:
        return sum

    for _ in range(m, n):
        a, b = b, (a + b ) % 10
        sum = (sum + b) % 10
            
    return sum

# if __name__ == '__main__':
    # input = sys.stdin.read()
from_, to = map(int, input().split())
print(fibonacci_partial_sum(from_, to))
