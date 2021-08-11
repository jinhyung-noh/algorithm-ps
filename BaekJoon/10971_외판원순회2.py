import sys
import itertools

n = int(input())
# make 2-dim list W
W = [[0]*n for _ in range(n)]
for i in range(n):
    arr = [int(k) for k in sys.stdin.readline().split()]
    for j in range(n):
        W[i][j] = arr[j]


# sol2: 시간초과
def minimum_cost1(W, n):
    min_cost = sys.maxsize
    for perm in itertools.permutations(range(0,n)):
        sum = 0
        is_impossible = False
        for j in range(n-1):
            # 갈 수 없는 도시 --> 망한 루트이므로 비용 터무니없게 설정
            if W[perm[j]][perm[j+1]] == 0:
                is_impossible = True
                break
            else:
                sum += W[perm[j]][perm[j+1]]

        if is_impossible:
            continue

        # 다시 시작도시로 돌아올 때
        if W[perm[n-1]][perm[0]] == 0:
            sum = sys.maxsize
        else:
            sum += W[perm[n-1]][perm[0]]
        
        if sum < min_cost:
            min_cost = sum
    return min_cost 

# using stack: 시간초과
def minimum_cost2(W, n):
    stack = [[i] for i in range(n-1, -1, -1)]
    min_cost = sys.maxsize

    while stack:
        a = stack.pop()
        # leaf node and comback route is OK: W[a[-1]][a[0]] != 0
        if len(a) == n:
            # calculate the cost
            if W[a[-1]][a[0]] != 0:
                sum = 0
                for j in range(1, n):
                    sum += W[a[j-1]][a[j]]
                sum += W[a[-1]][a[0]]
                min_cost = min(sum, min_cost)
            continue
        
        # add to stack
        for i in range(n-1, -1, -1):
            if i not in a and W[a[-1]][i] != 0:
                stack.append(a + [i])
    return min_cost
    

# using recursion: dfs
def minimum_cost3(W, n):

    def _dfs(depth, sum, current):
        # base case
        if depth == n:
            if W[current][start_point] != 0:
                min_cost[0] = min(min_cost[0], sum+W[current][start_point])
            return
        # recursive call
        for next in range(n):
            if not visited[next] and W[current][next] != 0:
                visited[next] = True
                _dfs(depth+1, sum+W[current][next], next)
                visited[next] = False
    
    min_cost = [sys.maxsize]
    visited = [False] * n

    for start_point in range(n):
        visited[start_point] = True
        _dfs(1, 0, start_point)
        visited[start_point] = False

    return min_cost[0]


print(minimum_cost3(W, n))


