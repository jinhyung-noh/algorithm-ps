def 특정거리의도시찾기():
    import sys
    from collections import deque

    # inputs
    N, M, K, X = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        dep, dest = map(int, sys.stdin.readline().split())
        graph[dep].append(dest)

    # global variables
    visited = [False] * (N+1)
    answers = []
    visited[X] = True
    Q = deque([(X, 0)])     # (도시, 거리)

    # BFS
    while Q:

        curr, dist = Q.popleft()

        # 원하는 결과: 거리가 K
        if dist == K:
            answers.append(curr)
            continue

        # 원하는 결과 아닐때 --> 방문하지 않은 인접 도시 방문(거리++)
        for next in graph[curr]:
            if not visited[next]:
                visited[next] = True        # 방문처리
                Q.append( (next, dist+1) )  # 큐에 추가

    # 출력
    if answers:
        answers.sort()
        return print(*answers, sep='\n')
    return print(-1)

특정거리의도시찾기()