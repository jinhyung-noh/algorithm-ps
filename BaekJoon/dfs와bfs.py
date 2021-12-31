def solution():

    import sys
    from collections import defaultdict, deque
    input = sys.stdin.readline

    #############################################
    # input
    N, M, V = map(int, input().split())
    # 인접리스트 구성
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a) # 양방향

    # 정렬
    for key in graph:
        graph[key].sort()
    ##############################################

    visited_dfs = [False] * (N+1) # 0번 인덱스는 버려! 
    dfs_print = []
    def _dfs(curr):
        # 현재 노드에 방문표시
        visited_dfs[curr] = True
        # 방문한 노드 기록
        dfs_print.append(curr)
        
        # 인접한 노드들 중 방문표시 안된것 방문
        for next in graph[curr]:
            if not visited_dfs[next]:
                _dfs(next)


    visited_bfs = [False] * (N+1)
    bfs_print = []
    def _bfs():
        # 큐 V부터 시작
        visited_bfs[V] = True
        q = deque([V]) 

        while q:
            # 현재 노드
            curr = q.popleft()
            # 출력 기록
            bfs_print.append(curr)

            # 연결된 노드 방문
            for next in graph[curr]:
                # 방문안된 노드만 방문처리하고 큐에 넣음
                if not visited_bfs[next]:
                    visited_bfs[next] = True
                    q.append(next)

        return
    
    _bfs() # bfs 탐색 시작
    _dfs(V) # V부터 dfs 탐색 시작
    print(*dfs_print, sep=' ')
    print(*bfs_print, sep=" ")
    return

solution()