import sys
sys.setrecursionlimit(100000)

def 연결요소의개수():
    # input: 양방향-연결리스트 형태로 받는다
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    # curr에 연결된 노드들을 모두 방문하고 방문 처리하는 함수
    def _dfs(curr):

        # 현재 노드 방문 처리
        visited[curr] = True

        # 방문하지 않은 자식 노드 방문
        for next in graph[curr]:
            if not visited[next]:
                _dfs(next)

    # global variables
    visited = [False] * (N+1)   # 방문 여부 표시
    cnt = 0                     # 연결된 그래프의 개수

    for V in range(1, N+1):     # 방문하지 않은 노드이면 cnt를 하나 올리고
        if not visited[V]:      # 그 노드에 연결된 노드들을 모두 방문처리한다!
            cnt += 1
            _dfs(V)

    return print(cnt)

연결요소의개수()