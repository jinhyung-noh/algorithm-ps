import sys
from bisect import bisect_left

def two_neutral_fluids():

    # input
    N = int(sys.stdin.readline())
    fluids = list(map(int, sys.stdin.readline().split()))
    fluids.sort()

    minimum_abs_PH = sys.maxsize
    minimum_fluids = None 

    for idx in range(N):
        # binary search: find candidates for pair fluid
        idx_pair = bisect_left(fluids, -fluids[idx])

        # exception case1: idx_pair == N
        if idx_pair == N:
            idx_pair = N-1
        # exception case2: find itself
        if idx_pair == idx:
            candidates = (idx_pair-1, idx_pair+1)
        elif idx_pair - 1 == idx:
            candidates = (idx_pair - 2, idx_pair)
        else:
            candidates = (idx_pair-1, idx_pair)
        
        # check
        for candidate in candidates:    # 2 cycle
            if (0 <= candidate < N) and abs(fluids[idx] + fluids[candidate]) < minimum_abs_PH:
                minimum_abs_PH = abs(fluids[idx] + fluids[candidate])
                minimum_fluids = (fluids[idx], fluids[candidate])
                # terminate condition: minimum_abs_PH == 0 
                if minimum_abs_PH == 0:
                    break

    return sorted(minimum_fluids)

print(*two_neutral_fluids())



















