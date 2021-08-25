import sys
from collections import defaultdict, deque


# using queue
def music_queue(N, graph, in_degree):

    # enque nodes with 0 indegree
    q = deque()
    for node in range(1, N+1):
        if in_degree[node] == 0:
            q.append(node)

    # topological sorting using queue
    # remove nodes with 0 indegree --> enque new nodes with 0 indegree
    result = []
    while q:
        curr = q.popleft()
        result.append(curr)

        for next in graph[curr]:
            in_degree[next] -= 1
            if in_degree[next] == 0:
                q.append(next)


    if len(result) == N:
        print(*result, sep='\n')
    else:
        print(0)
    return


# using dfs(recursion)
def music_dfs(N, graph, in_degree):

    def _dfs(curr):

        # 순환구조시 탐색 안함
        if has_cycle[0]:
            return

        visited[curr] = True
        # 현재까지의 경로 기록
        route.append(curr)

        for next in graph[curr]:
            # 순환구조 판단
            if next in route:
                has_cycle[0] = True
            if not visited[next]:
                _dfs(next)
        # 노드 탐색 완료시 경로에서 pop하고, result에 추가
        route.pop()
        result.append(curr)


    visited = [False] * (N+1)   # 노드 방문 여부 기록
    route = []                  # 탐색 경로 기록
    has_cycle = [False]         # 순환구조여부 파악
    result = []

    for node in range(N+1):
        if not in_degree[node]: # 진입차수 0인 노드 탐색
            _dfs(node)

    if has_cycle[0]:
        print(0)
    else:
        print(*result[-1:-N-1:-1], sep='\n')
    return 


# inputs
N, M = map(int, sys.stdin.readline().split())
graph  = defaultdict(list)
in_degree = [0] * (N+1)
for _ in range(M):
    nums = list(map(int, sys.stdin.readline().split()))
    for i in range(1, nums[0]):
        in_degree[nums[i+1]] += 1
        graph[nums[i]].append(nums[i+1])

# 택 1
# music_queue(N, graph, in_degree)
# music_dfs(N, graph, in_degree)