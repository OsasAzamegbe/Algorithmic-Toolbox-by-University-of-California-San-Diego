# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    a = 0
    b = 1
    result = 0

    for _ in range(1, n):
        result = a + b
        a, b = b, result

    return result

n = int(input())
print(calc_fib(n))
