import sys

def largest_interval():

    def _divided_into(num: int):
        "num만큼의 간격이 주어질 때 몇개까지 나뉘는가"
        sum = 0
        cnt = 0
        for interval in intervals:
            sum += interval
            if sum >= num:
                cnt += 1
                sum = 0
        return cnt

    def _binary_search(left: int, right: int):
        """find largest interval between `left` and `right`"""

        while left <= right:
            center = (left + right) // 2

            divided_into = _divided_into(center)

            if divided_into >= D:   # 분할수만큼 이상 나오면 안될때까지 올린다 
                left = center + 1
            else:
                right = center - 1
        return right

    # input
    N, C = list(map(int, sys.stdin.readline().split()))
    houses = [0] * N
    for i in range(N):
        houses[i] = int(sys.stdin.readline())
    houses.sort()

    # make interval array
    intervals = [0] * (N-1)
    for i in range(N-1):
        intervals[i] = houses[i+1] - houses[i]
        
    # searching
    # 1부터 이론상 최대 분할 간격까지 이진탐색
    
    return _binary_search(1, (houses[-1] - houses[0]) // (C-1))

print(largest_interval())