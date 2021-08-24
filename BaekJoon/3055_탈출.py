import sys
from collections import deque

def escape():

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
    waters = []
    hedgehog = None
    field = [None] * R
    for i in range(R):
        field[i] = list(sys.stdin.readline().strip())
        for j in range(C):
            if field[i][j] == '*':
                waters.append((i, j, '*'))
            elif field[i][j] == 'S':
                hedgehog = (i, j, "S")
    ############################################

    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([False] + waters + [hedgehog])
    time = 0
    survived = False
    while len(queue) > 1:
        curr = queue.popleft()

        # update time
        if not curr:
            time += 1
            queue.append(False)
            continue
        
        x, y, identity = curr
        if _spread(x, y, identity):
            survived = True
            break
    
    if survived:
        return time
    return "KAKTUS"

print(escape())