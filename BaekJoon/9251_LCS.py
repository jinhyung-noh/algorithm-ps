import sys
from collections import defaultdict
# sys.setrecursionlimit(1000000)

# def LCS(s1, s2):

#     # base case
#     if s1 == "" or s2 == "":
#         return 0

#     # case 1
#     if s1[-1] == s2[-1]:
#         return LCS(s1[:-1], s2[:-1]) + 1

#     # case 2
#     return max(LCS(s1[:-1], s2), LCS(s1, s2[:-1]))

# def LCS2(s1, s2):

#     def _helper(i: int, j: int):

#         # base case
#         if i == -1 or j == -1:
#             return 0

#         # using cache
#         if table[(i, j)]:
#             return table[(i, j)]

#         # case1
#         if s1[i] == s2[j]:
#             table[(i, j)] = _helper(i-1, j-1) + 1
#             return table[(i, j)]

#         table[(i, j)] = max(_helper(i, j-1), _helper(i-1, j))
#         return table[(i, j)]
    
#     table = defaultdict(int)
#     return _helper(len(s1)-1, len(s2)-1)

def LCS3(s1, s2):
    n, m = len(s1), len(s2)
    lcs_table = [[0] * (m + 1) for _ in range(n + 1)]

    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                lcs_table[i][j] = lcs_table[i-1][j-1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i][j-1], lcs_table[i-1][j])
    
    return lcs_table[n][m]



            

# inputs
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

print(LCS3(s1, s2))
