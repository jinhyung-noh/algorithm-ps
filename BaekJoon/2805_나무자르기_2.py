def 나무자르기():
    import sys
    input = sys.stdin.readline

    # 높이가 h일때 목재의 양을 구해주는 함수
    def wood_at_h(trees, h):
        sum = 0
        # 나무 리스트를 순회하면서 목재의 양을 구한다
        for tree in trees:
            if (tree > h):     # h보다 큰 나무들만 계산
                sum += (tree - h)
        return sum

    # inputs
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    # 이 부분은 원래
    # trees.sort()
    # low = trees[0]
    # high = trees[-1] 
    # 로 했는데 찾고자 하는 높이가 어제 누나가 말했던 대로 0 <= H <= max(trees) 범위 내라서
    # 굳이 정렬할 필요 없는 것 같아요
    low = 0
    high = max(trees)

    while low <= high:
        mid = (low + high) // 2

        cut_wood = wood_at_h(trees, mid) # h = mid일때 구한 목재의 양

        # 원하는 경우
        if cut_wood == M:
            return mid
        
        # 아닐경우 --> 탐색 이어나간다
        if cut_wood > M:  # 목표보다 많은 목재 --> 탐색범위 위쪽 반으로 설정
            low = mid + 1
        else:             # 목표 미달 목재 --> 탐색범위 아래쪽 반으로 설정
            high = mid - 1

    # 탐색 마친 경우: low가 더 큰값 --> low를 반환?? 
    # 이 경우가 제일 애매하고 어떤 값을 처리해야 할지 모르겠다
    # low, high 둘다 돌려보고 맞는거 했습니다 --> 
    return high 

print(나무자르기())