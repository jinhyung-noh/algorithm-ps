def 섬의개수():
    import sys
    sys.setrecursionlimit(10000)

    def _dfs(x, y):
        # 방문 표시
        field[x][y] = 0

        # 다음 지점 방문: 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상 (시계방향) 순서
        for i in range(8):
            nx, ny = x + dr[i][0], y + dr[i][1]
            if 0 <= nx < H and 0<= ny < W and field[nx][ny] == 1:
                _dfs(nx, ny)

    answers = []
    # 다음 방향 (dx, dy): 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상 (시계방향) 순서
    dr = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    # 각 케이스마다 입력을 받고 섬의 개수를 센 뒤 기록한다
    while True:
        # input
        W, H = map(int, sys.stdin.readline().split())

        # terminate condition
        if [W, H] == [0, 0]:
            break

        field = [None] * H
        for i in range(H):
            field[i] = list(map(int, sys.stdin.readline().split()))

        cnt = 0
        for i in range(H):
            for j in range(W):
                # 육지(1) 발견 --> 섬의 개수 올리고, dfs로 탐색하며 연결된 섬을 모두 바다(0)로 만들어준다
                if field[i][j] == 1:
                    cnt += 1
                    _dfs(i, j)

        # 탐색 종료 --> 섬의 개수 기록
        answers.append(cnt)

    return print(*answers, sep='\n')

섬의개수()



    




