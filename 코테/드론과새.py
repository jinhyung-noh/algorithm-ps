

def drone_n_bird():
    import sys
    input = sys.stdin.readline

    def _dfs(x, y):
        # 방문처리
        visited[x][y] = True

        # drone
        if field[x][y] == 'o':
            drone_and_bird[0] += 1
        # bird
        if field[x][y] == 'v':
            drone_and_bird[1] += 1

        # next search
        for i in range(4):
            nx, ny = x + dr[i][0], y + dr[i][1]
            # field 범위 내에 있고, 벽이 아니고 방문하지 않은 경우 탐색
            if 0<=nx<R and 0<=ny<C and field[nx][ny] != '#' and not visited[nx][ny]:
                _dfs(nx, ny)

        return

    # inputs
    R, C = map(int, input().split())
    field = [None] * R
    for i in range(R):
        field[i] = list(input().strip())
    ###########################################

    dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * C for _ in range(R)]
    drones = 0
    birds = 0
    # field 전체 탐색 시작
    for i in range(R):
        for j in range(C):
            # 벽이 아니거나 방문하지 않은 곳이면 탐색 시작
            if field[i][j] != '#' and not visited[i][j]:
                drone_and_bird = [0, 0]
                _dfs(i, j)
                # 탐색 후 새가 살아있는 영역 --> 새 count
                if drone_and_bird[1] > 0 and drone_and_bird[1] >= drone_and_bird[0]:
                    birds += drone_and_bird[1]
                # 탐색 후 드론이 살아있는 영역 --> 드론 count
                if drone_and_bird[0] > drone_and_bird[1]:
                    drones += drone_and_bird[0]

    return print(drones, birds) 

drone_n_bird()
