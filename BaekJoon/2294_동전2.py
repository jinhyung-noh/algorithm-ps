import sys
from collections import deque, defaultdict

def minimum_coins():

    # 시간초과(DFS)
    # def _dfs(level, target):
    #     # terminate cond
    #     if level > minimum_level[0]:
    #         return

    #     # base cases
    #     if target < 0:
    #         return
    #     if target == 0:
    #         minimum_level[0] = min(minimum_level[0], level)
    #         return
        
    #     # recursive call
    #     for coin in coins:
    #         _dfs(level+1, target - coin)

    # inputs

    n, k = list(map(int, sys.stdin.readline().split()))
    coins = [None] * n
    for i in range(n):
        coins[i] = int(sys.stdin.readline())
    coins = sorted(set(coins), reverse=True)

    queue = deque([(1, k - coin) for coin in coins])
    visited = defaultdict(lambda: False)

    while queue:
        level, target = queue.popleft()
        if visited[target]:
            continue

        visited[target] = True
        if target < 0:
            continue
        elif target == 0:
            return level
        
        for coin in coins:
            queue.append((level+1, target - coin))

    return -1
print(minimum_coins())



