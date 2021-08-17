import sys

def visible_sticks():

    # inputs
    N = int(sys.stdin.readline())
    sticks = [0] * N
    for i in range(N):
        sticks[i] = int(sys.stdin.readline())
    

    cnt = 1
    temp = sticks[-1]
    for idx in range(N-1, -1, -1):
        if sticks[idx] > temp:
            cnt += 1
            temp = sticks[idx]
    return cnt

print(visible_sticks())