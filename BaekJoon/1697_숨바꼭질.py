import sys
from collections import deque, defaultdict

# inputs
N, K = map(int, sys.stdin.readline().split())

def bfs(N, K):

    if N == K:
        return 0

    def f1(x):
        return x - 1

    def f2(x):
        return x + 1

    def f3(x):
        return 2 * x


    visited = defaultdict(lambda: False)
    visited[N] = True
    functions = [f1, f2, f3]
    q = deque([(0, N)])

    while q:
        time, curr = q.popleft()

        for i in range(3):
            next = functions[i](curr) 

            if next == K:
                return time + 1

            if not visited[next] and 0 <= next <= 100000:
                visited[next] = True
                q.append((time+1, next))

print(bfs(N, K))