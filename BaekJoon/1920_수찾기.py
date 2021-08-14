import sys

def binary_search(arr: list, target: int):
    """return 1 if target is in arr else return 0"""

    def _binary_search_helper(left: int, right: int):
        # base case 1
        if left > right:
            return 0
        
        center = (left + right) // 2
        # base case2
        if arr[center] == target:
            return 1

        # recursive call
        if arr[center] < target:
            return _binary_search_helper(center+1, right)
        else:
            return _binary_search_helper(left, center - 1)

    return _binary_search_helper(0, len(arr) -1)

# 입력 받기
n = int(sys.stdin.readline())
arr = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
answers = [None] * m
nums = list(map(int, sys.stdin.readline().split()))
for i in range(m):
    answers[i] = binary_search(arr, nums[i])

# 출력하기
for answer in answers:
    print(answer)



