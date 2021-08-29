import sys

def house_numbering(N, arr):

    def _dfs(x, y):
        
        cnt = 1
        for i in range(4):
            nx, ny = x + dr[i][0], y + dr[i][1]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != '0':
                arr[nx][ny] = '0'
                cnt += _dfs(nx, ny)

        return cnt

    dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != '0':
                arr[i][j] = '0'
                result.append(_dfs(i, j))
    
    result.sort()
    # outputs
    print(len(result))
    print(*result, sep='\n')


# inputs
N = int(sys.stdin.readline())
arr = [None] * N
for i in range(N):
    arr[i] = list(sys.stdin.readline().strip())

house_numbering(N, arr)

