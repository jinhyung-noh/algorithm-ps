import sys


def plus_123(n: int):

    def _dfs(target: int):
        # base case1
        if target < 0:
            return
        if target == 0:
            cnt[0] += 1
            return
        
        # recursive call
        for next_number in range(3, 0, -1):
            _dfs(target - next_number)

    cnt = [0]
    for first_number in range(3, 0, -1):
        _dfs(n - first_number)
    return cnt[0]

# 입력 받기
N = int(sys.stdin.readline())
nums = [0] * N
for i in range(N):
    nums[i] = int(sys.stdin.readline())


# 출력하기
for i in range(N):
    print(plus_123(nums[i]))
