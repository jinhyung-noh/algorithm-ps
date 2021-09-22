def solution(scoville, K):
    from heapq import heapify, heappush, heappop

    # heaify
    heapify(scoville)
    cnt = 0
    first, second = 0, 0

    while True:
        first = heappop(scoville)
        # 남아있으면 second를 뽑는다
        if (len(scoville) > 0):
            second = heappop(scoville)
        # 하나도 없다면 first(최종 매운 음식)의 스코빌 지수와 K를 비교한다
        else:
            if first < K:
                return -1

        if (first >= K):
            break

        cnt += 1
        # 섞은 음식을 heap에 추가한다
        heappush(scoville, first + 2 * second)

    return cnt


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))