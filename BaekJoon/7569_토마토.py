import sys
from collections import deque

def tomato():

    #################################################
    # inputs
    M, N, H = list(map(int, sys.stdin.readline().split()))
    tomatoes = [[[None] for _ in range(N)] for _ in range(H)]
    rotten_tomatoes = deque([False])
    normal_tomatoes = 0
    for x in range(H):
        for y in range(N):
            tomatoes[x][y] = list(map(int, sys.stdin.readline().split()))
            # count normal and rotten tomaoes
            for z in range(M):
                if tomatoes[x][y][z] == 0:
                    normal_tomatoes += 1
                if tomatoes[x][y][z] == 1:
                    rotten_tomatoes.append((x, y, z))
    #################################################


    # all tomatoes are rotten at start --> return
    if normal_tomatoes == 0:
        return 0

    dr = [(-1, 0, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0)]
    time = 0
    while normal_tomatoes > 0 and len(rotten_tomatoes) > 1:

        curr = rotten_tomatoes.popleft()
        # today start
        if not curr:
            time += 1
            rotten_tomatoes.append(False)
            continue

        x, y, z = curr
        for i in range(6):
            nx, ny, nz = x + dr[i][0], y + dr[i][1], z + dr[i][2]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M \
                and tomatoes[nx][ny][nz] == 0:
                tomatoes[nx][ny][nz] = 1   # 익은 토마토로 변신
                normal_tomatoes -= 1
                rotten_tomatoes.append((nx, ny, nz))
                if normal_tomatoes == 0:
                    break

    ###################
    if normal_tomatoes == 0:
        return time
    return -1

print(tomato())




