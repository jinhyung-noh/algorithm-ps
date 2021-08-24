import sys
from collections import deque

def BFS(arr):
    N = len(arr)
    M = len(arr[0])
    dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 1)])  # (x, y, cnt)
    
    while queue:
        x, y, cnt = queue.popleft()
        # terminate condition
        if x == N-1 and y == M-1:
            break

        for i in range(4):
            nx, ny = x + dr[i][0], y + dr[i][1]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '1':

                arr[nx][ny] = '0'   # 탐색 표시
                queue.append((nx, ny, cnt+1))
    return cnt


# inputs
N, M = list(map(int, sys.stdin.readline().split()))
arr = [None] * N
for i in range(N):
    arr[i] = list(sys.stdin.readline().strip())


print(BFS(arr))