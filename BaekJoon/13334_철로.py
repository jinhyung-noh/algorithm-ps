import sys
from heapq import heappop, heappush
from bisect import bisect_right

# 시간초과
# def rail():

#     # inputs
#     N = int(sys.stdin.readline())
#     people = [None] * N
#     for i in range(N):
#         people[i] = sorted(map(int, sys.stdin.readline().split()))
#     d = int(sys.stdin.readline())
        
#     # sorting
#     people.sort(key=lambda x: x[0])

#     # searching
#     maximum = 0
#     start = -sys.maxsize
#     for i in range(N):
#         if people[i][0] == start:
#             continue

#         if people[i][0] > start:
#             cnt = 0
#             start = people[i][0]

#         while i < N and people[i][0] <= start + d:
#             if people[i][1] <= start + d:
#                 cnt += 1
#             i += 1

#         maximum = max(maximum, cnt)
    
#     print(maximum)

def rail2():

    # inputs
    N = int(sys.stdin.readline())
    people = [None] * N
    for i in range(N):
        people[i] = sorted(map(int, sys.stdin.readline().split()))
    d = int(sys.stdin.readline())
        
    # sorting
    people.sort(key=lambda x: (x[1], x[0]))

    # searching
    maximum = 0
    heap = []   # min heap: people in range

    for i in range(N):
        # pop out of range: heap[0] is minimum x0
        while heap and heap[0][0] < people[i][1] - d:
            heappop(heap)
        # push if current person is in range
        if people[i][1] - people[i][0] <= d:
            heappush(heap, people[i])
        maximum = max(maximum, len(heap))

    print(maximum)
rail2()