import sys

# 폐기: 중간 기록 저장(트리 아닌 중간에 이어지면 중복되게 센다)
# def counting(N, graph, visited, result):

#     def _dfs(curr):
#         sum = 0
#         for next in range(1, N+1):
#             if graph[curr][next] and not visited[next]:
#                 if result[next]:
#                     sum += (result[next] + 1)
#                 else:
#                     sum += (_dfs(next) + 1)
#         visited[curr] = True
#         result[curr] = sum
#         return sum
    
#     for start in range(1, N+1):
#         _dfs(start)
#     return result

def counting(N, graph):

    def _dfs(curr):
        visited[curr] = True
        cnt = 0
        for next in range(1, N+1):
            if graph[curr][next] and not visited[next]:
                cnt += (_dfs(next) + 1)
        return cnt
    
    results = [0] * (N+1)

    for i in range(1, N+1):
        visited = [False] * (N+1)
        results[i] = _dfs(i)
    return results


# input
N, M = list(map(int, sys.stdin.readline().split()))
bigger = [[0] * (N + 1) for _ in range(N + 1)]
smaller = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    num1, num2 = list(map(int, sys.stdin.readline().split()))
    bigger[num1][num2] = 1
    smaller[num2][num1] = 1


# print(counting(N, bigger))
# print(counting(N, smaller))

nums_bigger_than = counting(N, bigger)
nums_smaller_than = counting(N, smaller)
##############33
print(nums_bigger_than)
print(nums_smaller_than)
imposibles = 0
bd = (N+1) // 2
for i in range(1, N+1):
    if nums_smaller_than[i] >= bd or nums_bigger_than[i] >= bd:
        imposibles += 1

print(imposibles)