import sys


def 파일합치기():

    def minimum_cost(N, files):

        def sub_sums(i, j):
            if sub_sums_table[i][j]:
                return sub_sums_table[i][j]
            sub_sums_table[i][j] = sum(files[i:j+1])
            return sub_sums_table[i][j]


        table = [[0] * (N) for _ in range(N)]
        sub_sums_table = [[0] * N for _ in range(N)]
        for j in range(1, N):
            for i in range(j-1, -1, -1):
                minimum = sys.maxsize
                for k in range(i, j):
                    minimum = min(minimum, table[i][k] + table[k+1][j] + sub_sums(i, j))
                table[i][j] = minimum
        return table[0][N-1]

    # inputs
    T = int(sys.stdin.readline())
    results = [0] * T
    for i in range(T):
        N = int(sys.stdin.readline())
        files = list(map(int, sys.stdin.readline().split()))
        results[i] = minimum_cost(N, files)

    print(*results, sep="\n")

파일합치기()

