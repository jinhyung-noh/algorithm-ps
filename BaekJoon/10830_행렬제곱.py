import sys

def matrix():

    def _ij_element(X: list[list[int]], Y: list[list[int]], i: int, j: int):
        sum = 0
        for k in range(N):
            sum += (X[i][k] * Y[k][j])
        return sum % 1000

    def _matrix_mult(X: list[list[int]], Y: list[list[int]]):
        temp = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                temp[i][j] = _ij_element(X, Y, i, j)
        return temp

    # input
    N, B = list(map(int, sys.stdin.readline().split()))
    A = [None] * N
    for i in range(N):
        A[i] = list(map(int, sys.stdin.readline().split()))
    
    
    # 단위행렬로 초기화
    result = [[0]* N for _ in range(N)]
    for i in range(N):
        result[i][i] = 1

    B = bin(B)
    for bit in B[2:]:
        result = _matrix_mult(result, result)
        if bit == '1':
            result = _matrix_mult(result, A)
    
    # 출력
    for i in range(N):
        print(" ".join(map(str, result[i])))
    return

matrix()



