import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict


# 오답(행렬 계산)
# # inputs

# N = int(sys.stdin.readline())
# M = int(sys.stdin.readline())
# arr = [[0] * (N+1) for _ in range(N+1)]
# for _ in range(M):
#     num1, num2, num3 = list(map(int, sys.stdin.readline().split()))
#     arr[num1][num1] = -1
#     arr[num1][num2] = num3

# for i in range(1, N):
#     if arr[i][i] == -1:     # i는 중간부품
#         for j in range(i+1, N+1):     # i가 포함된 다른 부품들 에서 i 제거
#             if arr[j][i] != 0:
#                 for k in range(1, N):
#                     arr[j][k] = arr[j][k] + arr[i][k] * arr[j][i]

# # print(arr)
# for idx in range(1, N):
#     if arr[N][idx] != 0:
#         print(idx, arr[N][idx])


def toy_assembly():

    def _dfs(curr):
        # base case:
        if curr == N:
            return 1
        if records[curr] != 0:
            return records[curr]

        # recursive call
        sum = 0
        for next in range(1, N+1):
            if arr[curr][next]:
                sum += arr[curr][next] * _dfs(next)
        records[curr] = sum
        return sum
    
    # inputs
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        num1, num2, num3 = list(map(int, sys.stdin.readline().split()))
        arr[num2][num1] = num3
    # calculate indegree: arr[i][0]
    for i in range(1, N+1):
        arr[i][0] = sum([1 if arr[j][i] else 0 for j in range(1, N+1)])


    records = defaultdict(int)
    result = defaultdict(int)
    for i in range(1, N+1):
        if not arr[i][0]:   # consider nodes whose indgree == 0
            result[i] = _dfs(i)

    # outputs
    for base_part in sorted(result.keys()):
        print(base_part, result[base_part])

toy_assembly()



