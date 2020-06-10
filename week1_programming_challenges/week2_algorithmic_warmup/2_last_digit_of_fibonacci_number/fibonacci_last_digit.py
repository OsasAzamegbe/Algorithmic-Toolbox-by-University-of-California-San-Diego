# Uses python3
import sys

def get_fibonacci_last_digit(n):
    # last digits of fibonacci numbers repeat after 60
    n %= 60
    if n <= 1:
        return n
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10


    return current

# if __name__ == '__main__':
    # input = sys.stdin.read()
n = int(input())
print(get_fibonacci_last_digit(n))
