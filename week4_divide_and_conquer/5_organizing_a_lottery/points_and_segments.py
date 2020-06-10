# Uses python3
import sys
import random

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    line = []
    points_counter = {}
    
    for i in range(len(starts)):
        line.append((starts[i], "left"))
        line.append((ends[i], "right"))
    for num in points:
        line.append((num, "point"))
        points_counter[num] = 0
    line.sort()
    # print(line, "\n")

    left_counter = 0

    for item in line:
        if item[1] == "left":
            left_counter += 1
        elif item[1] == "right":
            left_counter -= 1
        else:
            points_counter[item[0]] = left_counter
    
    # print(points_counter)
    for i in range(len(points)):
        cnt[i] = points_counter[points[i]]    

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
# # data = list(map(int, '3 2 0 5 -3 2 7 10 1 6'.split()))
# data = [5, 4, 17, 19, 6, 14, 16, 19, 2, 5, 5, 8, 19, 1, 19, 14]
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

 
# count = 0
# while True:
#     n = random.randrange(1, 50001)
#     m = random.randrange(1, 50001)
#     data = [n, m] + [random.randrange(-100000000, 100000001) for _ in range(n)]
#     for i in range(3, 2 * n + 2, 2):
#         data.insert(i, random.randrange(data[i - 1], 100000001))
#     data += [random.randrange(-100000000, 100000001) for _ in range(m)]

#     starts = data[2:2 * n + 2:2]
#     ends   = data[3:2 * n + 2:2]
#     points = data[2 * n + 2:]
#     #use fast_count_segments

#     cnt = fast_count_segments(starts, ends, points)
#     # cnt_2 = naive_count_segments(starts, ends, points)
#     print("data:", data, "\nmy solution:", cnt,  "\nNaive solution:", cnt_2, "\n------------------------------------------------------------------------\n")
#     count += 1
#     if cnt != cnt_2:
#         print("WRONGGGGG!!!!!!!!!")
#         break
#     if count >= 1:
#         print("No Erroneous solutions.")
#         break

