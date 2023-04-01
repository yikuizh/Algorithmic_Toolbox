from sys import stdin
from collections import namedtuple
import numpy as np

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points=[]
    # use while here:
    for i in range(len(segments)-1):
        right = segments[i][1]
        left = segments[i][0]
        overlap =[left,right]
        for j in range(1,len(segments)):
            if right >= segments[j][0]: # if overlap 
                overlap[0]=segments[j][0]
                overlap[1]=np.minimum(right, segments[j][1]) # find the overlap segment
        #if points:
        if not points:
            points.append(overlap[0])
        else:
            for num in points:
                if overlap[0]!=num:
                    points.append(overlap[0])

    return points

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)