# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort(key=lambda x: x.end)
    points.append(segments[0].end)
    for s in segments: 
        if not (s.start <= points[-1] and points[-1] <= s.end):       
            points.append(s.end)
        
    return points

if __name__ == '__main__':  
    input = sys.stdin.read()
    n, *data = map(int, input.split())
# n, *data = map(int, input().split())
# n, *data = map(int, "3 1 3 2 5 3 6".split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
