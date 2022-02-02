def 정수삼각형():
    import sys
    input = sys.stdin.readline

    N = int(input())
    # dp[i][j] : i번째 행, j번째 숫자까지 올때까지 최대 합 저장한 것
    dp = [[] for _ in range(N)]

    for i in range(N):
        ith_numbers = list(map(int, input().split()))
        # 예외처리: 첫번째 행
        if i == 0:
            dp[i].append( ith_numbers[0] )
            continue

        for j in range(len(ith_numbers)):
            left, right = 0, 0
            if j > 0 :  # 직전 행(i-1번째)에서 왼쪽
                left = dp[i-1][j-1]
            if j < i: # 직전 행(i-1번째)에서 오른쪽
                right = dp[i-1][j]
            # 왼쪽, 오른쪽 중 더 큰것과 해당 숫자의 합 저장
            dp[i].append( max(left, right) + ith_numbers[j] )
        
    # 마지막 dp행에서 가장 큰 값 출력
    print(max(dp[-1]))

정수삼각형()

