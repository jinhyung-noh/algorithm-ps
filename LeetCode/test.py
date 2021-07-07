from collections import defaultdict
graph = defaultdict(list, {
    # 1: [2,3,4],
    # 2: [5],
    # 3: [5],
    # 4: [],
    # 5: [6,7],
    # 6: [],
    # 7:[3],
    1: [2,3],
    2:[1]
})

route = []
def dfs(node):
    while graph[node]:
        dfs(graph[node].pop(0))
    route.append(node)

dfs(1)
print(route[::-1])