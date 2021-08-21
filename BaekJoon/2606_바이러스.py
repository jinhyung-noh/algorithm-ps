import sys
from collections import defaultdict, deque

def virus_DFS(graph: dict, N: int):

    def _dfs(curr: int):

        visited[curr] = True
        for next in graph[curr]:
            if not visited[next]:
                _dfs(next)
        return

    visited = [False] * (N + 1)
    _dfs(1)
    return sum(visited) - 1

def virus_BFS(graph: dict, N: int):

    visited = [False] * (N + 1)
    queue = deque([1])
    visited[1] = True

    while queue:
        curr = queue.popleft()

        for child in graph[curr]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)
    return sum(visited) - 1


def virus_DFS_stack(graph: dict, N: int):

    stack = [1]
    visited = [False] * (N + 1)

    while stack:
        curr = stack.pop()
        if visited[curr]:
            continue
        visited[curr] = True

        for child in graph[curr]:
            if not visited[child]:
                stack.append(child)
    
    return sum(visited) - 1

# input
graph = defaultdict(list)
N = int(sys.stdin.readline())
n = int(sys.stdin.readline())
for _ in range(n):
    com1, com2 = list(map(int, sys.stdin.readline().split()))
    graph[com1].append(com2)
    graph[com2].append(com1)

# print(virus_DFS(graph, N))
# print(virus_BFS(graph, N))
print(virus_DFS_stack(graph, N))


