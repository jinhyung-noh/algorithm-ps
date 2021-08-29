import sys


def 동전0():

    # inputs
    N, target = map(int, sys.stdin.readline().split())
    coins = [0] * N
    for i in range(N-1, -1, -1):
        coins[i] = int(sys.stdin.readline())

    cnt = 0
    for coin in coins:
        cnt += target // coin
        target %= coin
        if target == 0:
            break

    print(cnt)

동전0()