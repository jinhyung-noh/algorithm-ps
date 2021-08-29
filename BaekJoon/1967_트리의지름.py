import sys
sys.setrecursionlimit(100000)
from collections import defaultdict


def max_diameter():

    # inputs
    n = int(sys.stdin.readline())
    # undirected graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for _ in range(n-1):
        num1, num2, weight = map(int, sys.stdin.readline().split())
        graph[num1].append((num2, weight))
        graph[num2].append((num1, weight))
        in_degree[num1] += 1
        in_degree[num2] += 1

    # to find a leaf node; using indegree == 1
    one_indegrees = [i for i in in_degree if in_degree[i] == 1] # indgree 1 찾기
    start = one_indegrees[0] if one_indegrees else 0            # indexError 방지

    def _dfs(curr, curr_weight):

        visited[curr] = True
        branches = [0]
        for next, next_weight in graph[curr]:
            if not visited[next]:
                route[0] += next_weight
                branches.append(_dfs(next, next_weight))
                route[0] -= next_weight

        # update global max diameter
        # 루트로부터의 거리, 각각의 서브트리에서 리프까지의 최장거리들 중 가장 큰 2개 택
        max_dia[0] = max(max_dia[0], sum(sorted(branches + route[:], reverse=True)[:2]))
        return max(branches) + curr_weight
        
    # exception case: tree with only one node
    if not graph:
        return 0

    visited = defaultdict(lambda: False)
    max_dia = [0]
    route = [0]

    _dfs(start, graph[start][0][1])
    return max_dia[0]


def max_diameter2():

    # inputs
    N = int(sys.stdin.readline())
    # directed graph
    graph = defaultdict(list)
    for _ in range(N-1):
        parent, child, weight = map(int, sys.stdin.readline().split())
        graph[parent].append((child, weight))

    # global variables
    max_dia = [0]

    def _helper(curr, weight):

        sub_lens = [0]
        for next, next_weight in graph[curr]:
            sub_lens.append(_helper(next, next_weight))

        # sub-tree에서 생기는 v자와 global max_dia 비교
        # 각각의 sub-tree에서 leaf까지의 최장거리들 중 2개의 합
        sub_lens.sort(reverse=True)
        max_dia[0] = max(max_dia[0], sum(sub_lens[:2]))

        # 현재 노드에서 leaf까지의 최장거리 반환
        # sub-tree값들 중 가장 큰 값과 자신의 weight를 더한 값
        return sub_lens[0] + weight

    _helper(1, 0)
    return max_dia[0]


print(max_diameter2())