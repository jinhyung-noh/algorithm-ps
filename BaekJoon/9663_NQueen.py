import sys

N = int(sys.stdin.readline())


# position of a queen: pos[i] = j
# i: i-th column
# j: j-th row
pos = [0] * N

# check existing j-th row
check_row = [False] * N

# check existing diagonal1: //// direction
check_diag1 = [False] * (2 * N - 1)

# check existing diagonal2: \\\\ direction
check_diag2 = [False] * (2 * N - 1)

def set(i):
    """set i-th column"""
    if i == N:
        return 1

    result = 0
    for j in range(N):
        if not check_row[j] and\
            not check_diag1[i+j] and\
            not check_diag2[i-j+N-1]:

            pos[i] = j
            check_row[j] = check_diag1[i+j] = check_diag2[i-j+N-1] = True
            result += set(i+1)
            check_row[j] = check_diag1[i+j] = check_diag2[i-j+N-1] = False
    return result



print(set(0))
