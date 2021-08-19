import sys
from heapq import heappush, heappop

def card_sort():

    min_heap = []
    # inputs
    N = int(sys.stdin.readline())
    # heapify
    for _ in range(N):
        heappush(min_heap, int(sys.stdin.readline()))

    total_cnt = 0
    for _ in range(N-1):
        sum = 0
        sum += heappop(min_heap)
        sum += heappop(min_heap)
        total_cnt += sum
        heappush(min_heap, sum)
    
    print(total_cnt)

card_sort()