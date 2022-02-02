def 내려가기():
    import sys
    input = sys.stdin.readline    

    def _next_max_dp(prev_max, numbers):
        """이전 max_dp -> 새 max_dp"""
        result = [0,0,0]
        result[0] = numbers[0] + max(prev_max[:2])
        result[1] = numbers[1] + max(prev_max)
        result[2] = numbers[2] + max(prev_max[1:])
        return result

    def _next_min_dp(prev_max, numbers):
        """이전 min_dp -> 새 min_dp"""
        result = [0,0,0]
        result[0] = numbers[0] + min(prev_max[:2])
        result[1] = numbers[1] + min(prev_max)
        result[2] = numbers[2] + min(prev_max[1:])
        return result

    N = int(input())
    max_dp = [0,0,0]
    min_dp = [0,0,0]

    for i in range(N):
        # 새 3 숫자 받을 때마다 max_dp, min_dp 갱신
        numbers = list(map(int, input().split()))
        max_dp = _next_max_dp(max_dp, numbers)
        min_dp = _next_min_dp(min_dp, numbers)

    print(max(max_dp), min(min_dp))

내려가기()