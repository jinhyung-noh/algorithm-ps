# 11724번 연결 요소의 개수
import sys
sys.setrecursionlimit(10000)

# input
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# global variables
visited = [False] * (N+1)
cnt = 0

def _dfs(curr):
    # 방문 표시
    visited[curr] = True

    # 연결된 다음 노드 방문
    for next in graph[curr]:
        if not visited[next]:
            _dfs(next)

# 연결된 sub-graph개수 세기
for start in range(1, N+1):
    if not visited[start]:
        # 개수++
        cnt += 1
        _dfs(start)

print(cnt)