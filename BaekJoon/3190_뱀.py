import sys
from collections import deque

def snake_lifetime():

    def _next_head():
        # snake : [direction:int, body: deque([(x0, y0), (x1, y1), ...])]
        x_next = snake[1][-1][0]
        y_next = snake[1][-1][1]

        if snake[0] == 0:   # up
            x_next -= 1
        elif snake[0] == 1: # right
            y_next += 1
        elif snake[0] == 2: # down
            x_next += 1
        else:               # left
            y_next -= 1

        return [x_next, y_next]
        

    ##########################################
    # inputs
    N = int(sys.stdin.readline())
    num_apples = int(sys.stdin.readline())

    apples = [None] * num_apples
    for i in range(num_apples):
        apples [i] = list(map(lambda x:x-1, map(int, sys.stdin.readline().split())))

    num_direction_change = int(sys.stdin.readline())
    direction_change = [None] * num_direction_change    # [('time', direction), ... ,]
    for i in range(num_direction_change):
        direction_change[i] = sys.stdin.readline().split()
    ##########################################

    time = 0
    snake = [1, deque([(0,0)])] # [direction of head, coordinates of snake]
                                # direction: 0(up), 1(right), 2(down), 3(left)
    idx_direction_change = 0
    while True:
        next_head = _next_head()

        # terminate conition1: check next_head is wall
        if 0 > next_head[0] or N <= next_head[0] or\
            0 > next_head[1] or N <= next_head[1]:
            break
        # terminate condition2: check next_head is in snake itself
        if next_head in snake[1]:
            break

        # next_head is apple position--> remove that apple pos
        if next_head in apples:
            apples.remove(next_head)
        else:           # next_head is not apple pos --> cut tail
            snake[1].popleft()
        snake[1].append(next_head)

        # next time
        time += 1
        # check time to change direction
        if idx_direction_change < num_direction_change and time == int(direction_change[idx_direction_change][0]):
            if direction_change[idx_direction_change][1] == 'L':
                snake[0] = (snake[0] - 1) % 4
            else:
                snake[0] = (snake[0] + 1) % 4
            idx_direction_change += 1

    return time + 1

print(snake_lifetime())