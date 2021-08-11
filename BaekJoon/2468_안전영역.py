import sys
from copy import deepcopy

# recursion depth: 1000000
sys.setrecursionlimit(1000000)

# inputs
N = int(sys.stdin.readline())
Area = [None] * N
max_height = 0
for i in range(N):
    Area[i] = list(map(int, sys.stdin.readline().split()))
    max_height = max(max_height, max(Area[i]))


def  safe_area(Area: list[list[int]], k: int):

    def _dfs(x: int, y: int):
        # less than k: submerged area --> terminate searching
        if Area[x][y] <= k:
            return

        # mark and search more: CW(clockwise order)
        Area[x][y] = k
        if 0 < x:
            _dfs(x-1, y)
        if y < N - 1:
            _dfs(x, y+1)
        if x < N - 1:
            _dfs(x+1, y)
        if 0 < y:
            _dfs(x, y-1)

    N = len(Area)
    cnt_safe = 0
    for x in range(N):
        for y in range(N):
            if Area[x][y] > k:
                cnt_safe += 1
                _dfs(x, y)

    return cnt_safe

max_areas = 0
for k in range(max_height):
    max_areas = max(max_areas, safe_area(deepcopy(Area), k))


print(max_areas)