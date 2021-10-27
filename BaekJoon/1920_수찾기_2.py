def 수찾기():
    import sys
    input = sys.stdin.readline

    # inputs
    N = int(input())
    nums = list(map(int, input().split()))
    M = int(input())
    targets = list(map(int, input().split()))

    # helper function: binary-search
    def _bs(target):

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            # 찾은경우
            if nums[mid] == target:
                return 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        # 못찾은 경우
        return 0


    # *** 중요 *** 
    # 정렬 후 -> 이분탐색
    nums.sort()
    answer = [None] * M

    # 각각 target마다 있는지 확인
    for i in range(M):
        answer[i] = _bs(targets[i])

    print(*answer, sep='\n')

수찾기()