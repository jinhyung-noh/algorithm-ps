from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == '.' and c[nx][ny] == 0:
                        c[nx][ny] = c[x][y] + 1
                        q.append([nx, ny])
                    elif a[nx][ny] == 'D':
                        print(c[x][y])
                        return
            qlen -= 1
        # 다음번 물에 대해 bfs 수행
        water()

    print("Kaktus")
    return

# 처음 wq를 받았을 때 원소 만큼만 bfs 수행한다/ wq에 append는 계속 하여 다음에 탐색할 물 추가는 함
# while wq가 아닌 while qlen
def water():
    qlen = len(wq)
    while qlen:
        x, y = wq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == '.':
                    a[nx][ny] = '*'
                    wq.append([nx, ny])
        qlen -= 1

# inputs
n, m = map(int, input().split())    # n by m matrix
a = [list(map(str, input())) for _ in range(n)]
c = [[0]*m for _ in range(n)]
q, wq = deque(), deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            x1, y1 = i, j
            a[i][j] = '.'
        elif a[i][j] == '*':
            wq.append([i, j])

print(q)
print(wq)
water()
# bfs(x1, y1)
print(a)