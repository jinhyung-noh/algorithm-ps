def 포도주시식():
    import sys
    input = sys.stdin.readline
    # dp[n] : n번째가 최대가 될때 포도주의 양

    # dp[n-1]
    # dp[n-2] + amount[n]
    # dp[n-3] + amount[n-1] + amount[n] 3 값 중 더 큰 값이 dp[n]

    N = int(input())
    amount = [0] * N
    for i in range(N):
        amount[i] = int(input())

    dp = [0] * N
    try:
        dp[0] = amount[0]
        dp[1] = dp[0] + amount[1]
        dp[2] = max(amount[0] + amount[1], amount[0] + amount[2], amount[1] + amount[2])
        for i in range(3, N):
            dp[i] = max(dp[i-1]     \
                    , dp[i-2] + amount[i] \
                    , dp[i-3] + amount[i-1] + amount[i])
    except:
        pass

    print(dp[-1])

포도주시식()