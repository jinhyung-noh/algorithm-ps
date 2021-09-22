def 가장긴바이토닉부분수열():
    import sys

    def _make_dp(nums, dp):
        for i in range(N):
            temp = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    temp = max(temp, dp[j] + 1)
                dp[i] = temp

    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    dp1 = [1] * N
    dp2 = [1] * N
    maxlen = 0

    _make_dp(nums, dp1)
    _make_dp(nums[::-1], dp2)

    for i in range(N):
        maxlen = max(maxlen, dp1[i] + dp2[N-1-i] - 1)
    print(maxlen)
    return

가장긴바이토닉부분수열()