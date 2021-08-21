import sys
sys.setrecursionlimit(10000000)
from collections import defaultdict

# 메모리 초과(인접행렬)
# def DFS(arr, start):
#     N = len(arr) - 1
#     visited = [False] * (N + 1)
#     parents = [None] * (N + 1)

#     def _dfs(curr):

#         for next in range(1, N + 1):
#             if arr[curr][next] and not visited[next]:
#                 arr[next][curr] = 0
#                 visited[next] = True
#                 parents[next] = curr
#                 _dfs(next)
    
#     _dfs(start)
#     return parents[2:]


# # input
# N = int(sys.stdin.readline())
# arr = [[0]*(N+1) for _ in range(N+1)]
# for _ in range(N - 1):
#     n1, n2 = list(map(int, sys.stdin.readline().split()))
#     arr[n1][n2] = arr[n2][n1] = 1
# print(*DFS(arr, 1))

def DFS(graph, N, start):
    visited = defaultdict(lambda: False)
    parents = defaultdict(lambda: None)

    def _dfs(curr):

        for next in graph[curr]:
            if not visited[next]:
                visited[next] = True
                parents[next] = curr
                _dfs(next)
    
    _dfs(start)
    # ouptuts
    for i in range(2, N+1):
        print(parents[i])
    return

def DFS_stack(graph, N, start):
    visited = defaultdict(lambda: False)
    parents = defaultdict(lambda: None)
    stack = [start]

    while stack:
        curr = stack.pop()
        visited[curr] = True

        for next in graph[curr]:
            if not visited[next]:
                parents[next] = curr
                stack.append(next)

    # ouptuts
    for i in range(2, N+1):
        print(parents[i])
    return


# input
N = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(N - 1):
    n1, n2 = list(map(int, sys.stdin.readline().split()))
    graph[n1].append(n2)
    graph[n2].append(n1)
# DFS(graph, N, 1)
DFS_stack(graph, N, 1)
