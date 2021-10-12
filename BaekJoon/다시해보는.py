# 4963번 섬의 개수
import sys
sys.setrecursionlimit(10000)

# dfs helper function
def _dfs(x, y):
    # marking
    visited[x][y] = True

    # 인접한 육지 방문
    for i in range(8):
        nx, ny = x + dr[i][0], y + dr[i][1]
        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and field[nx][ny] == 1:
            _dfs(nx, ny)

# global variables
answers = []
dr = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# 각 케이스별로 반복
while True:

    # inputs
    W, H = map(int, sys.stdin.readline().split())
    # terminate condition
    if W == 0 and H == 0:
        break
    visited = [[False] * W for _ in range(H)]
    field = [None] * H
    for i in range(H):
        field[i] = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and field[i][j] == 1:
                cnt += 1
                _dfs(i, j)
    
    answers.append(cnt)

print(*answers, sep='\n')