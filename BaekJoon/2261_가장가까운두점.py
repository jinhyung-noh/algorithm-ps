import sys
from collections import deque

def shortest_distance():

    def _dist_sqr(pt1: list[int], pt2: list[int]):
        return (pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2

    # input
    N = int(sys.stdin.readline())
    points = [None] * N
    for i in range(N):
        points[i] = list(map(int, sys.stdin.readline().split()))

    # sort: x coordinate ascending order
    points.sort(key=lambda x: x[0])
    min_d_sqr = _dist_sqr(points[0], points[1])
    candidates = deque()

    # search and update min_d_sqr
    for i in range(N):
        # pick out candidates
        while candidates and candidates[0][0] < points[i][0] - min_d_sqr ** 0.5:
            candidates.popleft()
        # update min_d
        for candidate in candidates:
            min_d_sqr = min(min_d_sqr, _dist_sqr(candidate, points[i]))

        candidates.append(points[i])

    return min_d_sqr

print(shortest_distance())

