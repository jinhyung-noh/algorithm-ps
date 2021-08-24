import sys
from collections import deque

def escape():

    # bfs: waters, hedgehogs에 따라 다르게 수행
    def _spread(x, y, id):

        for i in range(4):
            nx, ny = x + dr[i][0], y + dr[i][1]
            if 0 <= nx < R and 0 <= ny < C:

                # water case
                if id == '*' and (field[nx][ny] == '.' or field[nx][ny] == 'S'):
                    field[nx][ny] = '*' # 
                    queue.append((nx, ny, '*'))

                # hedgehog case
                elif id == 'S':
                    # check hedgehog reaches to beaver
                    if field[nx][ny] == 'D':
                        return True
                    elif field[nx][ny] == '.':
                        field[nx][ny] = 'S'
                        queue.append((nx, ny, 'S'))
        return False

    ###################################################
    # inputs
    R, C = list(map(int, sys.stdin.readline().split()))
    waters = []         # 초기 water의 좌표들
    hedgehog = None     # 처음 고슴도치의 좌표
    field = [None] * R
    for i in range(R):
        field[i] = list(sys.stdin.readline().strip())
        for j in range(C):
            if field[i][j] == '*':
                waters.append((i, j, '*'))
            elif field[i][j] == 'S':
                hedgehog = (i, j, "S")
    ###################################################

    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([False] + waters + [hedgehog])    # False는 시간 사이의 간격
    time = 0
    survived = False    # 비버소굴에 도착했는지
    while len(queue) > 1:
        curr = queue.popleft()

        # update time   
        # deque([False, (waters ...), (hedgehogs...)] 일때 False가 leftpop되면 이전 time은 끝나고 time+1로 갱신
        if not curr:
            time += 1
            queue.append(False)
            continue
        
        # waters. hedgehogs일 경우 bfs 수행하고 비버소굴에 도착했는지 확인
        x, y, identity = curr
        if _spread(x, y, identity):
            survived = True
            break
    
    if survived:
        return time
    return "KAKTUS"

print(escape())