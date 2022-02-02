def 팰린드롬():
    import sys
    input = sys.stdin.readline

    N = int(input())
    numbers = list(input().split())

    # dp 만들기: dp[s][e] = dp[s+1][e-1] and numbers[s] == numbers[e]
    # 길이가 1인 것부터 N인것까지 채워나가기
    dp = [[0] * N for _ in range(N)]
    # 길이가 1
    s = 0
    e = 0
    while e < N:
        dp[s][e] = 1
        s += 1
        e += 1
    # 길이가 2
    s = 0
    e = s + 1
    while e < N:
        dp[s][e] = int(numbers[s] == numbers[e])
        s += 1
        e += 1
    # 길이가 k
    for length in range(3, N+1):
        s = 0
        e = s + length - 1
        while e < N:
            dp[s][e] = int(dp[s+1][e-1] and numbers[s] == numbers[e])
            s += 1
            e += 1

    M = int(input())
    answers = [0] * M
    for i in range(M):
        # S, E를 입력받아서 dp를 보고 palindrom인지 확인하기
        S, E = map(int, input().split())
        answers[i] = dp[S-1][E-1]

    print(*answers, sep="\n")

팰린드롬()