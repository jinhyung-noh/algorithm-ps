import sys


def 외판원순회():

    # bit-masking functions
    def isIn(A: int, i: int):
        return (A & (1 << (i-1))) != 0

    def diff(A: int, i: int):
        return (A & ~(1 << (i-1)))

    # A의 원소 개수 반환
    def count(A, n):
        cnt = 0
        for i in range(n):
            if (A & (1 << i)):
                cnt += 1
        return cnt

    def min_path(A: int, i: int):   
        # A: integer interpreted as binary number --> representation of a subset
        # i: starting point (destination is 1)

        next = 0
        # minimum = sys.maxsize
        minimum = sys.maxsize
        for j in range(1, N):
            if isIn(A, j):
                temp = W[i][j] + D[j][diff(A, j)]
                if temp < minimum:
                    minimum = temp
                    next = j
        return minimum, next

    # inputs
    N = int(sys.stdin.readline())
    W = [None] * N
    for i in range(N):
        W[i] = [j if j != 0 else sys.maxsize for j in list(map(int, sys.stdin.readline().split()))]
        W[i][i] = 0

    size = 2 ** (N-1)
    D = [[0] * size for _ in range(N)]
    P = [[0] * size for _ in range(N)]

    # base case(A: 공집합)
    for i in range(1, N):
        D[i][0] = W[i][0]

    # fill D matrix order of 1 .. N-2(number of elements of A)
    # 원소의 개수가 k인 것만 관심을 가질 예정이다
    for k in range(1, N-1):
        # k가 정해지면
        # 모든 A들 중에
        for A in range(1, size):
            # 원소의 개수가 k인 것만 거른다
            if count(A, N-1) == k:
                # n(A) == k
                # 'start' is not in A
                for start in range(1, N):
                    if not isIn(A, start):
                        D[start][A], P[start][A] = min_path(A, start)

    # last case; start is 1 --> D[1][size-1]
    D[0][size-1], P[0][size-1] = min_path(size-1, 0)

    print(D[0][size-1])
    return

외판원순회()




