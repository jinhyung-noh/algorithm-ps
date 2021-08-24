import sys
from collections import deque, defaultdict

def topological_sort():

    # inputs
    N, M = list(map(int, sys.stdin.readline().split()))
    graph = defaultdict(lambda: [0, []])       # [num of 'in's, [connected nodes]]

    for _ in range(M):
        num1, num2 = list(map(int, sys.stdin.readline().split()))
        graph[num1][1].append(num2)     # num1 --> num2: out
        graph[num2][0] += 1     # num1 --> num2: in

    # Set of all nodes with no incoming edge
    queue = deque([i for i in range(1, N+1) if not graph[i][0]])
    ##################################
    print("#####################")
    print(queue)
    result = []

    while queue:
        curr = queue.popleft()
        result.append(curr)
        # remove connection of 'curr'
        for next in graph[curr][1]:
            graph[next][0] = max(0, graph[next][0] - 1)
            if not graph[next][0]:
                queue.append(next)
    return result

print(*topological_sort())