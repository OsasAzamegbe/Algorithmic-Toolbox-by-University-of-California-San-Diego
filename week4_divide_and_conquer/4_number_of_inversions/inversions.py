# Uses python3
import sys

def get_number_of_inversions(a):
    number_of_inversions = 0
    size =len(a)
    if size == 1:
        return number_of_inversions, a
    ave = size // 2
    b_count, b = get_number_of_inversions(a[:ave])
    number_of_inversions += b_count
    c_count, c= get_number_of_inversions(a[ave:])
    number_of_inversions += c_count
    #write your code here
    a_count, a_ = compare(b, c)
    number_of_inversions += a_count
    return number_of_inversions, a_

def compare(b, c):
    d = []
    count = 0
    while b and c:
        if b[0] <= c[0]:
            d.append(b.pop(0))
        else:
            count += len(b)
            d.append(c.pop(0))
    
    if c:
        d += c
    elif b:
        d += b
    # print("d:", d)
    return count, d


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
# n, *a = list(map(int, '6 9 8 7 3 2 1'.split()))
# n, *a = list(map(int, '5 6 1 5 2 3'.split()))
# b = n * [0]
    count, a = get_number_of_inversions(a)
    print(count)