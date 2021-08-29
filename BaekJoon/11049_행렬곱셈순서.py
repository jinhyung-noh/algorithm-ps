import sys

def minimum_matrix_operation():

    # inputs
    N = int(sys.stdin.readline())
    matrices = [None] * N
    for i in range(N):
        matrices[i] = list(map(int, sys.stdin.readline().split()))

    # table[i][j]: i-th-Matrix * ... * j-th-Matrix 의 최소 연산 횟수
    table = [[0] * N for _ in range(N)]

    for j in range(1, N):
        for i in range(j-1, -1, -1):
            candidate = sys.maxsize
            for k in range(i, j):
                candidate = min(candidate 
                                , matrices[i][0] * matrices[k][1] * matrices[j][1]
                                + table[i][k] + table[k+1][j])
            table[i][j] = candidate

    print(table[0][N-1])
    return

minimum_matrix_operation()