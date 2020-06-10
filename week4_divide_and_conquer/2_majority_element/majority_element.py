# Uses python3
import sys

def get_majority_element(a, left, right):
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]
    #write your code here
   
    a.sort()
    m = right//2
    if right % 2 == 0:   
        if a[m] == a[m - 1] and a.count(a[m]) > m:
            return True
    else:
        if (a[m] == a[m - 1] or a[m] == a[m + 1]) and a.count(a[m]) > m:
            return True
    return False

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
# n, *a = list(map(int, '7 1 1 1 3 5 5 5'.split()))

# if get_majority_element(a, 0, n) != -1:
    if get_majority_element(a, 0, n):
        print(1)
    else:
        print(0)

