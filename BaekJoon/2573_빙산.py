import sys
sys.setrecursionlimit(10000000)
from copy import deepcopy

def iceburg(arr, R, C):

    def _next_height(arr, x, y):
        cnt_zero = 0
        for i in range(4):
            next_x = x + dr[i][0]
            next_y = y + dr[i][1]
            if arr[next_x][next_y] == 0:
                cnt_zero += 1
        return max(0, arr[x][y] - cnt_zero)

    def _next_iceburg(arr, xl, xr, yl, yr):
        next = deepcopy(arr)
        for i in range(xl, xr+1):
            for j in range(yl, yr+1):
                next[i][j] = _next_height(arr, i, j)
        return next

        
    def cnt_iceburgs(xl, xr, yl, yr):

        def _dfs(x, y):
            for i in range(4):
                next_x, next_y = x + dr[i][0], y + dr[i][1]
                if xl <= next_x <= xr and yl <= next_y <= yr \
                    and arr[next_x][next_y] > 0:
                    arr[next_x][next_y] = 0     # 탐색 표시
                    _dfs(next_x, next_y)
        
        iceburgs = 0
        for i in range(xl, xr+1):
            for j in range(yl, yr+1):
                if arr[i][j] > 0:
                    iceburgs += 1
                    _dfs(i, j)
        return iceburgs

    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    time = 0
    xl, xr, yl, yr = 1, R-2, 1, C-2
    next_iceburg = _next_iceburg(arr, xl, xr, yl, yr)
    islands = cnt_iceburgs(xl, xr, yl, yr)
    while islands == 1:
        arr = next_iceburg
        # update margins
        try:
            while sum([arr[xl][j] for j in range(yl, yr+1)]) == 0: xl += 1
            while sum([arr[xr][j] for j in range(yl, yr+1)]) == 0: xr -= 1
            while sum([arr[i][yl] for i in range(xl, xr+1)]) == 0: yl += 1
            while sum([arr[i][yr] for i in range(xl, xr+1)]) == 0: yr -= 1
        except IndexError:      # zero islands
            return 0
        next_iceburg = _next_iceburg(arr, xl, xr, yl, yr)
        islands = cnt_iceburgs(xl, xr, yl, yr)
        time += 1

    return time


# inputs
R, C = list(map(int, sys.stdin.readline().split()))
arr = [None] * R
for i in range(R):
    arr[i] = list(map(int, sys.stdin.readline().split()))

print(iceburg(arr, R, C))
