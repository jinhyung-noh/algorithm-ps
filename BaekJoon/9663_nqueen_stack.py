import sys

# N = int(sys.stdin.readline())

N = 2

pos = [0] * N

stack = [0]
while stack:
    i = stack.pop()
    if i == N:
        print(pos)
        continue
    for j in range(N):
        pos[i] = j
        stack.append(i+1)



