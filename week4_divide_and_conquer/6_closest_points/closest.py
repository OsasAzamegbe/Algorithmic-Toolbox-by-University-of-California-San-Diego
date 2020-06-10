#Uses python3
import sys
import math
import random

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def minimum_distance(points):  
    #write your code here
    points.sort()
    # print(points)
    return section_min(points)

def section_min (points):
    pass
    size = len(points)
    if size <= 3:
        return brute_force(points)
    mid = size // 2
    left = points[:mid]
    right = points[mid:]
    left_min = section_min(left)
    right_min = section_min(right)
    d_min = min(left_min, right_min)
    divisor = (left[-1][0] + right[0][0]) / 2
    bound_min = boundary_min(left, right, divisor, d_min)

    return min(d_min, bound_min)

def boundary_min(left, right, divisor, d_min):
    bound_section = []
    for item in left[::-1]:
        if divisor - item[0] <= d_min:
            bound_section.append(item)
        else:
            break
    bound_section = bound_section[::-1]
    for item in right:
        if item[0] - divisor <= d_min:
            bound_section.append(item)
        else:
            break
    
    bound_section = sorted(bound_section, key=lambda x: x[1])
    ans = d_min

    for i in range(len(bound_section)):
        for j in range(i + 1, min(i + 8, len(bound_section))):
            if abs(bound_section[i][1] - bound_section[j][1]) <= d_min:
                ans = min(ans, distance(bound_section[i], bound_section[j]))
    return ans


def brute_force(points):
    d_min = distance(points[0], points[1])
    size = len(points)
    if size == 2:
        return d_min

    for i in range(size - 1):
        for j in range(i + 1, size):            
            d_min = min(d_min, distance(points[i], points[j]))
    
    return d_min

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
# data = list(map(int, '11 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4'.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = [(x[i], y[i]) for i in range(n)]
    print("{0:.9f}".format(minimum_distance(points)))

 
# count = 0
# while True:
#     n = random.randrange(2, 100)   
#     data = [n] + [random.randrange(-1000000000, 1000000001) for _ in range(2 * n)]
#     x = data[1::2]
#     y = data[2::2]
#     points = [(x[i], y[i]) for i in range(n)]
#     mine = "{0:.9f}".format(minimum_distance(points))
#     brute = "{0:.9f}".format(brute_force(points))
    
#     print("data:", data, "\nmy solution:", mine,  "\nNaive solution:", brute, "\n------------------------------------------------------------------------\n")
#     count += 1
#     if mine != brute:
#         print("WRONGGGGG!!!!!!!!!")
#         break
#     # if count >= 2:
#     #     print("No Erroneous solutions.")
#     #     break