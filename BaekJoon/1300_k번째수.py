# def k번째수():

#     import sys
#     from collections import defaultdict
#     input = sys.stdin.readline

#     N = int(input())
#     k = int(input())

#     # counter hash 만들기
#     hash = defaultdict(int);
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             hash[i * j] += 1


#     # 누적 hash 만들기
#     hash_keys = sorted(hash.keys())
#     temp = 0
#     for key in hash_keys:
#         hash[key] += temp
#         temp = hash[key]

#     # 이분탐색 
#     low = 0
#     high = len(hash_keys) - 1
#     while low < high:
#         mid = (low + high) // 2
#         # if (hash[mid] == k) :
#         #     return hash_keys[mid]

#         if (hash[hash_keys[mid]] < k) :
#             low = mid + 1
#         else:
#             high = mid

#     return hash_keys[low]

def k번째수():
    import sys
    input = sys.stdin.readline

    N = int(input())
    k = int(input())

    low = 1
    high = N * N
    while (low < high):
        mid = (low + high) // 2
        below_cnt = 0
        for i in range(1, N+1):
            below_cnt += min(mid // i, N)

        if (below_cnt < k):
            low = mid + 1 
        else:
            high = mid

    print(low)

    

print(k번째수())
