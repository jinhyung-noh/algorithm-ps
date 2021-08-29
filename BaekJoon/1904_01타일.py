import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict

# def zero_one(N: int):

#     def _helper(i: int):

#         # base case
#         if i == 1 or i == 2:
#             return i
        
#         # using cache
#         if cache[i]:
#             return cache[i]

#         # recursive call
#         cache[i] = (_helper(i-1) + _helper(i-2)) % 15746
#         return cache[i]

#     cache = defaultdict(int)
#     return _helper(N)

def zero_one2(N):

    if N == 1 or N == 2:
        return N

    cache = defaultdict(int)
    cache[1] = 1
    cache[2] = 2
    
    i = 3
    while i <= N:
        cache[i] = (cache[i-1] + cache[i-2]) % 15746
        i += 1

    return cache[N]


# inputs
N = int(sys.stdin.readline())

# outputs
# print(zero_one(N))
print(zero_one2(N))