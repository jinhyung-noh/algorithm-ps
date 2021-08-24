import sys
from collections import deque, defaultdict

# using BFS + 중간 기록
def minimum_coins():

    ################################################
    # inputs
    n, k = list(map(int, sys.stdin.readline().split()))
    coins = [None] * n
    for i in range(n):
        coins[i] = int(sys.stdin.readline())
    coins = sorted(set(coins), reverse=True)
    ################################################

    queue = deque([(0, k)])
    visited = defaultdict(lambda: False)

    while queue:

        level, target = queue.popleft()
        if visited[target]: # 이미 방문한 target
            continue        # 그 전에 나온 경우 이상의 동전이 필요할 것 --> 무시

        visited[target] = True  # 방문 표시
        if target < 0:          # target을 넘어서는 경우 --> 무시
            continue
        elif target == 0:       # 문제에서 원하는 경우
            return level        # 동전 수(level) 반환
        
        for coin in coins:      # target 이하 -->  bfs 계속 진행
            queue.append((level+1, target - coin))

    return -1   # 모든 경우 탐색 --> -1 반환

# using dynamic programming: others code
def minimum_coins2():
    # inputs 
    N, K = map(int, sys.stdin.readline().split())
    coins = sorted(set([int(sys.stdin.readline()) for _ in range(N)]))

    min_coins = [sys.maxsize] * (K+1) # min_coins[target] : target을 만들수 있는 최소 동전의 개수
    min_coins[0] = 0                  # min_coins[0]: 0원을 만들수 있는 최소 동전의 개수: 0

    for coin in coins:                  # 작은 코인부터
        for target in range(coin, K+1): # 코인 이상의 target 모두 확인: target-coin에서 동전 1개(coin)만 더하면 target이 됨을 이용
            min_coins[target] = min(min_coins[target], min_coins[target-coin] + 1)

    return min_coins[K] if min_coins[K] != sys.maxsize else -1


# print(minimum_coins())
# print(minimum_coins2())