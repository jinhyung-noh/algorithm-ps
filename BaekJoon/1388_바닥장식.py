def 바닥장식():
    import sys

    # 입력
    N, M = map(int, sys.stdin.readline().split())
    field = [None] * N
    for i in range(N):
        field[i] = list(sys.stdin.readline().strip())

    # '-' 타일 탐색하는 함수
    def _dfs_right(x, y):
        # ''으로 마킹
        field[x][y] = ''

        # 오른쪽으로 탐색
        if y+1 < M and field[x][y+1] == '-':
            _dfs_right(x, y+1)

    # '|'타일 탐색하는 함수
    def _dfs_down(x, y):
        # ''으로 마킹
        field[x][y] = ''

        # 아래로 탐색
        if x+1 < N and field[x+1][y] == '|':
            _dfs_down(x+1, y)

    # 전체 타일 탐색
    cnt = 0                  # 타일 개수
    for i in range(N):
        for j in range(M):
            # 탐색 완료된 타일 건너뛰기
            if field[i][j] =='':
                continue
            # '-' 타일 발견 --> 오른쪽 탐색
            if field[i][j] == '-':
                _dfs_right(i, j)
            # '|' 타일 발견 --> 아래쪽 탐색
            else:
                _dfs_down(i, j)
            # 타일 개수 갱신
            cnt += 1

    # 결과 출력
    print(cnt)

바닥장식()


    

    