import sys
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
        # base case: 완제품인 경우
        if curr == N:
            return 1
        # 이미 방문한 노드일 경우 dfs 진행하지 않고 기록된 값 사용
        if records[curr] != 0:
            return records[curr]

        # recursive call
        sum = 0
        for next in range(1, N+1):
            # 하위 노드의 값들을 취합하여 반환
            if arr[curr][next]:
                sum += arr[curr][next] * _dfs(next)
        # 현재 노드 방문 처리 및 값 기록
        records[curr] = sum
        return sum
    
    ###################################################
    # inputs
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        num1, num2, num3 = list(map(int, sys.stdin.readline().split()))
        arr[num2][num1] = num3
    base_parts = [] # 기본 부품들 기록
    # arr[i][0] 에 i번째 노드의 진입차수 기록(진입차수가 0인 부품: 기본부품)
    for i in range(1, N+1):
        arr[i][0] = sum([1 if arr[j][i] else 0 for j in range(1, N+1)])
        if not arr[i][0]:
            base_parts.append(i)
    ###################################################


    records = defaultdict(int)  # records[i]: 완제품에서 필요한 i번째 부품의 개수
    for base_part in base_parts:
        _dfs(base_part)
        print(base_part, records[base_part])

toy_assembly()



