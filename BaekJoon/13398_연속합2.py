def 연속합2():
    import sys
    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))

    # 일단 양수(0 포함)인 것들은 합쳐놓기, 음수는 그대로
    new_numbers = []
    temp, positive_cnt = 0, 0
    for number in numbers:
        # 양수 나오면 계속 temp에 합해서 저장
        if number >= 0:
            positive_cnt += 1
            temp += number
        else:
            # 음수일 경우
            # positive_cnt가 있을때만 저장
            if positive_cnt > 0:
                new_numbers.append(temp)
            # 초기화
            new_numbers.append(number)
            temp, positive_cnt = 0, 0


    new_N = len(new_numbers)
    # dp 만들기
    dp = [[0]*new_N for _ in range(new_N)]
    # dp[s][e]: sum(new_numbers[s:e+1])
    # 길이가 1 (s == e)
    for i in range(new_N):
        dp[i][i] = new_numbers[i]
    
    for length in range(2, N+1):
        s = 0
        e = s + length - 1
        while e < new_N:
            dp[s][e] = dp[s][e-1] + new_numbers[e]
            s += 1
            e += 1

    # dp만들기2
    dp2 = [[0]*new_N for _ in range(new_N)]
    # dp2[s][e]: new_numbers[s:e+1] 중 가장 작은 음수
    for i in range(new_N):
        dp2[i][i] = new_numbers[i] if new_numbers[i] < 0 else 0
    
    for length in range(2, N+1):
        s = 0
        e = s + length - 1
        while e < new_N:
            dp2[s][e] = min(dp2[s][e-1], new_numbers[e])
            s += 1
            e += 1

    # dp1, dp2 합치기
    for s in range(new_N):
        for e in range(s, new_N):
            dp[s][e] = dp[s][e] - dp2[s][e]
    
    maxi = 0
    for row in dp:
        maxi = max(maxi, max(row))
    print(maxi)

연속합2()