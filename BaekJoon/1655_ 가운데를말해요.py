import sys
from heapq import heappush, heappop

# 시간초과
# from bisect import bisect_left
# def say_median1():

#     # inputs
#     N = int(sys.stdin.readline())
#     arr = []
#     answers = [0] * N
    
#     for i in range(N):
#         num = int(sys.stdin.readline())
#         idx = bisect_left(arr, num)
#         arr = arr[:idx] + [num] + arr[idx:]
#         answers[i] = arr[i//2]

#     # outputs
#     for answer in answers:
#         print(answer)

def say_median2():

    left = []       # max heap
    right = []      # min heap

    # inputs
    N = int(sys.stdin.readline())
    answers = [None] * N

    # start with left
    left.append(-int(sys.stdin.readline()))
    answers[0] = -left[0]

    for i in range(1,N):
        next_num = int(sys.stdin.readline())

        if i % 2 == 0:      # left push turn
            right_min = right[0]
            if next_num <= right_min:
                heappush(left, -next_num)
            else:
                heappush(left, -heappop(right))
                heappush(right, next_num)

        else:               # right push turn
            left_max = -left[0] 
            if next_num >= left_max:
                heappush(right, next_num)
            else:
                heappush(right, -heappop(left))
                heappush(left, -next_num)

        answers[i] = -left[0]

    # outputs
    for answer in answers:
        print(answer)


say_median2()