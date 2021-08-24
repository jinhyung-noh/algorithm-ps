import sys
sys.setrecursionlimit(10000000)
from collections import defaultdict, deque


# dfs using recursion
def DFS(graph, N, start):
    parents = defaultdict(lambda: None)
    parents[start] = True

    def _dfs(curr):
        # 현재 노드의 자식들 중 부모 노드가 기록되지 않은 것들 탐색
        # 부모 노드 기록된 노드 <==> 방문 노드
        for next in graph[curr]:
            if not parents[next]:
                parents[next] = curr    # 부모 노드 기록
                _dfs(next)
    
    _dfs(start)

    # ouptuts
    for i in range(2, N+1):
        print(parents[i])
    return

# dfs using stack
def DFS_stack(graph, N, start):
    parents = defaultdict(lambda: None)
    parents[start] = True
    stack = [start]

    while stack:
        curr = stack.pop()

        # 현재 노드의 자식들 중 부모 노드가 기록되지 않은 것들 탐색
        # 부모 노드 기록된 노드 <==> 방문 노드
        for next in graph[curr]:
            if not parents[next]:
                parents[next] = curr
                stack.append(next)

    # ouptuts
    for i in range(2, N+1):
        print(parents[i])
    return

# bfs
def BFS(graph, N, start):
    parents = [None] * (N+1)
    parents[start] = True 
    q = deque([start])

    while q:
        curr = q.popleft()
        # 현재 노드의 자식들 중 부모 노드가 기록되지 않은 것들 탐색
        # 부모 노드 기록된 노드 <==> 방문 노드
        for child in graph[curr]:
            if not parents[child]:
                parents[child] = curr
                q.append(child)
    
    # outputs
    for i in range(2, N+1):
        print(parents[i])
    return


# inputs
N = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(N - 1):
    n1, n2 = list(map(int, sys.stdin.readline().split()))
    graph[n1].append(n2)
    graph[n2].append(n1)


# 택 1
DFS(graph, N, 1)
DFS_stack(graph, N, 1)
BFS(graph, N, 1)