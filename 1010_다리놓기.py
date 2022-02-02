def 다리놓기():
    import sys
    import math
    input = sys.stdin.readline

    def _comb(n, m):
        # m C n = m C (m-n)
        if m//2 < n:
            n = m - n
        # 조합(m C n) 구하기
        # m C n = ( m * (m-1) * ... * (m-(n-1)) ) // (n!)
        comb = 1
        for i in range(n):
            comb *= (m-i)
        for i in range(n):
            comb //= (n-i)
        return comb

    T = int(input())
    answers = [0] * T
    for i in range(T):
        n, m = map(int, input().split())
        answers[i] = _comb(n, m)

    print(*answers, sep="\n")

다리놓기()