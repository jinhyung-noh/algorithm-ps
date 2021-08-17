import sys

# inputs
N, K = list(map(int, sys.stdin.readline().split()))

josephus = [0] * N
arr = list(range(1, N+1))

K -= 1
idx = 0
for i in range(N):
    idx += K
    if idx >= len(arr):
        idx %= len(arr)
    josephus[i] = arr[idx]
    del arr[idx]

# outputs
print('<', end='')
print(*josephus, sep=', ', end='')
print('>')

