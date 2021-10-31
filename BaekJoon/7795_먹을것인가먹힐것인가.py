import sys
input = sys.stdin.readline

def _bs(nums, k):
    # 이번 이진탐색은 같은 것을 찾는 것이 아니라
    # 찾고자 하는 수보다 작은 수 중에서 가장 큰 수를 찾는 것
    # 같은 경우도 왼쪽 탐색에 넣어준다(같은 거보다 작은 것을 찾고 싶으니까)
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        # 왼쪽 탐색
        # nums[mid] == k인 경우도 왼쪽 탐색에 넣어준다
        if nums[mid] >= k:
            high = mid - 1
        # 오른쪽 탐색
        else:
            low = mid + 1
    # 결국 high < low인 상황에서 탐색 종료
    return high

T = int(input())
answers = []
for _ in range(T):
    input() # 필요없는 입력 처리
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()
    cnt = 0
    for elem_A in A:
        # _bs(B, elem_A)는 찾고자 하는 수의 인덱스 --> 개수는 그 인덱스 + 1
        cnt += (_bs(B, elem_A) + 1)

    answers.append(cnt)

print(*answers, sep='\n')

