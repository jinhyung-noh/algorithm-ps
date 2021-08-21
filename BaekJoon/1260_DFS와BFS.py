import sys
from collections import defaultdict, deque

def DFS(graph: dict, startpoint: int):

    def _dfs(curr_node: int):

        visited[curr_node] = True
        result.append(curr_node)
        for next_node in graph[curr_node]:
            if not visited[next_node]:
                _dfs(next_node)

    visited = defaultdict(lambda: False)
    result = []
    _dfs(startpoint)
    return result

def DFS_stack(graph: dict, startpoint: int):

    result = []
    visited = defaultdict(lambda: False)
    stack = [startpoint]
    while stack:
        curr = stack.pop()
        if visited[curr]:
            continue
        visited[curr] = True
        result.append(curr)

        for child in graph[curr][::-1]:
            if not visited[child]:
                stack.append(child)
    return result

def BFS(graph: dict, startpoint: int):

    visited = defaultdict(lambda: False)
    temp = deque([startpoint])
    visited[startpoint] = True
    result = []
    while temp:
        curr = temp.popleft()
        result.append(curr)
        for next in graph[curr]:
            if not visited[next]:
                temp.append(next)
                visited[next] = True
    return result



# input
N, M ,v = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

# eliminate overlap and sort each values
for key in graph:
    graph[key] = sorted(set(graph[key]))


# print(*DFS(graph, v))
# print(*DFS_stack(graph, v))
# print(*BFS(graph, v))