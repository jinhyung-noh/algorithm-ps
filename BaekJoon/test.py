import sys
from collections import defaultdict, deque
def change_askii(alphabet):
    return ord(alphabet) % 65
def dfs(i, j):
    global maximum
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < r and 0 <= ny < c and not check[change_askii(graph[nx][ny])]:
            check[change_askii(graph[nx][ny])] = True
            maximum = max(maximum, sum(check))
            dfs(nx, ny)
            check[change_askii(graph[nx][ny])] = False
r, c = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(r)]
for i in range(r):
    input_val = sys.stdin.readline().rstrip()
    for j in input_val:
        graph[i].append(j)
check = [False for _ in range(26)]
maximum = 0
check[change_askii(graph[0][0])] = True
dfs(0, 0)

print(maximum)