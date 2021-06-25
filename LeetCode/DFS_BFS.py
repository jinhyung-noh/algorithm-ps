# DFS(Depth-First-Search)
# recursive - DFS
def recursive_dfs(graph, node, discovered=[]):
    discovered.append(node)
    for child_node in graph[node]:
        if child_node not in discovered:
            discovered = recursive_dfs(graph, child_node, discovered)
    return discovered

# iterative using stack - DFS
def iterative_dfs(graph, node):
    discovered = []
    stack = [node]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for child_node in graph[v]:
                stack.append(child_node)
    return discovered


# BFS(Breadth-First-Search)
# BFS can't run bu recursive way --> using queue
def iterative_bfs(graph, start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}   

# print(recursive_dfs(graph, 1))
# print(iterative_dfs(graph, 1))
# print(iterative_bfs(graph, 1))