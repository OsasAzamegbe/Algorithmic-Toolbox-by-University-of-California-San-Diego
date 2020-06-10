# Uses python3
import sys

def lcm_naive(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return a

    for l in range(b, a*b + 1, b):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

# if __name__ == '__main__':
#     input = sys.stdin.read()
a, b = map(int, input().split())
print(lcm_naive(a, b))

