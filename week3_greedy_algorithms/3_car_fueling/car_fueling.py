# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    n = len(stops)
    stops.insert(0, 0)
    stops.append(distance)
    
    j = 0
    refill = 0
    while j <= n:
        left = j
        while j <= n and stops[j + 1] - stops[left] <= tank:
            j += 1
        if left == j:
            return -1
        if j <= n:  
            refill += 1
  
    
    return refill


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
# d, m, _, *stops = map(int, input().split())
# print(compute_min_refills(d, m, stops))
