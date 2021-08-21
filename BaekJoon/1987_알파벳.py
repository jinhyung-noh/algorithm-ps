import sys
from collections import deque

def alphabets(arr: list[str], R: int, C: int):

    def alpha2num(alpha: str):
        return ord(alpha) % 65


    def _dfs(x: int, y: int):

        maximum[0] = max(maximum[0], sum(visited))

        for i in range(4):

            next_x, next_y = x + dr[i][0], y + dr[i][1]
            if 0 <= next_x < R and 0 <= next_y < C \
                and not visited[alpha2num(arr[next_x][next_y])]:

                visited[alpha2num(arr[next_x][next_y])] = True
                _dfs(next_x, next_y)
                visited[alpha2num(arr[next_x][next_y])] = False


    maximum = [0]
    visited = [False] * 26
    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ############################
    visited[alpha2num(arr[0][0])] = True
    _dfs(0, 0)
    visited[alpha2num(arr[0][0])] = False
    ############################
    return maximum[0]


##################################################
def alphabets2(arr: list[str], R: int, C: int):

    def alpha2num(alpha: str):
        return ord(alpha) % 65

    def _dfs(visited: list[bool], x: int, y: int, maximum: int):

        for i in range(4):

            next_x, next_y = x + dr[i][0], y + dr[i][1]
            if 0 <= next_x < R and 0 <= next_y < C \
                and not visited[alpha2num(arr[next_x][next_y])]:

                visited[alpha2num(arr[next_x][next_y])] = True
                maximum = max(maximum, _dfs(visited, next_x, next_y, sum(visited)))
                visited[alpha2num(arr[next_x][next_y])] = False

        return maximum

    visited = [False] * 26
    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    visited[alpha2num(arr[0][0])] = True
    return _dfs(visited, 0, 0, 1)

###########################################

def BFS(arr, R, C):

    maximum = 0
    queue = set([((0,0), arr[0][0])])
    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        curr, string = queue.pop()
        maximum = max(maximum, len(string))
        for i in range(4):
            next = (curr[0] + dr[i][0], curr[1] + dr[i][1])
            if 0 <= next[0] < R and 0 <= next[1] < C \
                and arr[next[0]][next[1]] not in string:
                queue.add((next, string+arr[next[0]][next[1]]))

    return maximum



# inputs
R, C = list(map(int, sys.stdin.readline().split()))
arr = [sys.stdin.readline().strip() for _ in range(R)]
# arr = [list(sys.stdin.readline().strip()) for _ in range(R)]

# print(alphabets(arr, R, C))
# print(alphabets2(arr, R, C))
print(BFS(arr, R, C))


