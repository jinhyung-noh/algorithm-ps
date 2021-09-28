def solution(n, edge):
    from collections import defaultdict, deque
    # 인접리스트 만들기
    graph = defaultdict(list)
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 전역변수
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)

    visited[1] = True     # node 1 방문처리
    q = deque([(1, 0)])   # (node, distance)

    # BFS
    while q:
        curr, dist = q.popleft()

        # 연결된 노드 중 방문하지 않은 노드 방문
        # (next, next_dist) 형태로 큐에 넣는다
        for next in graph[curr]:
            if not visited[next]:
                # 방문처리하고 거리 기록
                visited[next] = True
                distances[next] = dist + 1
                q.append((next, dist + 1))

    # distances에서 max(distances)의 개수를 센다
    return distances.count(max(distances))

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))