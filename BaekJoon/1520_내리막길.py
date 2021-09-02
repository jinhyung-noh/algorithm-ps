import sys
sys.setrecursionlimit(100000)


def 내리막길():

    def _dfs(x, y):

        # final destination
        if (x, y) == (N-1, M-1):
            table[x][y] = 1
            return table[x][y]

        # visited
        if table[x][y] != -1:
            return table[x][y]

        # recursive call
        sum = 0
        for i in range(4):
            nx, ny = x + dr[i][0], y + dr[i][1]
            if 0 <= nx < N and 0 <= ny < M and field[x][y] > field[nx][ny]:
                sum += _dfs(nx, ny)
        
        table[x][y] = sum
        return table[x][y]

    # inputs
    N, M = map(int, sys.stdin.readline().split())
    field = [None] * N
    for i in range(N):
        field[i] = list(map(int, sys.stdin.readline().split()))

    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    table = [[-1] * M for _ in range(N)]

    _dfs(0, 0)
    print(table[0][0])
    return

내리막길()