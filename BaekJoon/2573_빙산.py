import sys
sys.setrecursionlimit(10000000)

def iceburg(field, R, C):

    # 각 지점마다 동서남북 0의 개수를 세어 다음 높이를 반환하는 함수
    def _next_height(field, x, y):
        cnt_zero = 0
        if not field[x-1][y]: cnt_zero += 1
        if not field[x][y+1]: cnt_zero += 1
        if not field[x+1][y]: cnt_zero += 1
        if not field[x][y-1]: cnt_zero += 1
        return max(0, field[x][y] - cnt_zero)

    # field의 (xl <= x <= xr), (yl <= y <= yr) 부분의 모든 지점에서
    # 다음 시간의 높이를 구한 것들을 반환하는 함수
    def _melting_points(field, xl, xr, yl, yr):
        melting_points = []
        for i in range(xl, xr+1):
            for j in range(yl, yr+1):
                melting_points.append((i, j, _next_height(field, i, j)))
        return melting_points
    
    # 녹은 높이들을 field에 적용하는 함수
    def _next_iceburg(field, melting_points):
        for x, y, height in melting_points:
            field[x][y] = height

    # dfs로 빙산(섬)의 개수 파악하는 함수
    # field의 부분집합에서만 탐색 진행: (xl <= x <= xr), (yl <= y <= yr)
    def cnt_iceburgs(field, xl, xr, yl, yr):

        def _dfs(x, y):
            for i in range(4):
                next_x, next_y = x + dr[i][0], y + dr[i][1]
                # 주어진 범위 내 + 체크하지 않은 곳 + 물이 아닌 곳 모두 만족하면 탐색 진행
                # check_points는 field와 index가 다름에 주의
                if xl <= next_x <= xr and yl <= next_y <= yr \
                    and field[next_x][next_y] > 0\
                    and check_points[next_x-xl][next_y-yl] == 0:
                    check_points[next_x-xl][next_y-yl] = 1     # 탐색 표시
                    _dfs(next_x, next_y)
        
        # field의 부분집합에서만 탐색 진행: 
        # (xl <= x <= xr), (yl <= y <= yr)
        iceburgs = 0
        for i in range(xl, xr+1):
            for j in range(yl, yr+1):
                # check_points는 field와 index가 다름에 주의
                if field[i][j] > 0 and check_points[i-xl][j-yl] == 0:
                    check_points[i-xl][j-yl] = 1
                    iceburgs += 1
                    _dfs(i, j)
        return iceburgs

    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    time = 0
    # field의 부분집합을 결정하는 상한, 하한선들
    xl, xr, yl, yr = 1, R-2, 1, C-2

    while True:
        # 매 턴마다 섬이 녹으므로 불필요한 탐색을 줄이기 위해
        # 바다가 아닌 섬이 나올 때까지 상한, 하한선을 조정
        try:
            while sum([field[xl][j] for j in range(yl, yr+1)]) == 0: xl += 1
            while sum([field[xr][j] for j in range(yl, yr+1)]) == 0: xr -= 1
            while sum([field[i][yl] for i in range(xl, xr+1)]) == 0: yl += 1
            while sum([field[i][yr] for i in range(xl, xr+1)]) == 0: yr -= 1
        # IndexError는 상한, 하한선이 겹칠 때 --> 섬이 한번에 다 녹는 경우
        except IndexError:
            return 0

        # 매 턴 줄어든 탐색범위 만큼의 check points를 생성
        # 다만 check points는 field와 index 차이를 고려해야 함(cnt_iceburgs 함수)
        check_points = [[0] * (yr - yl + 1) for _ in range(xr - xl + 1)]
        # 빙산의 개수 
        islands = cnt_iceburgs(field, xl, xr, yl, yr)
        # 녹은 빙산 적용
        _next_iceburg(field, _melting_points(field, xl, xr, yl, yr))

        # 탈출조건
        if islands != 1:
            break
        time += 1
    return time

######################################################
# inputs
R, C = list(map(int, sys.stdin.readline().split()))
field = [None] * R
for i in range(R):
    field[i] = list(map(int, sys.stdin.readline().split()))
#######################################################

print(iceburg(field, R, C))
