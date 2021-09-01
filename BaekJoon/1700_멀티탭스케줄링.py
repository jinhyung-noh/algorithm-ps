import sys
from copy import copy

def 멀티탭스케줄링():
    # inputs
    N, M = map(int, sys.stdin.readline().split())
    appliances =  list(map(int, sys.stdin.readline().split()))

    curr = set()
    cnt = 0
    for i in range(M):

        if len(curr) < N:
            curr.add(appliances[i])
            continue

        # curr에 없는 새로운 것이 왔을 때
        if appliances[i] not in curr:

            # 마지막으로 나오는 것 찾기
            temp = copy(curr)
            for j in range(i+1, M):
                if appliances[j] in temp:
                    temp.remove(appliances[j])
                if len(temp) <= 1:
                    break
            # temp에서 끝까지 살아남은 것 curr에서 제거
            # 가장 마지막에 나오는 것 혹은 앞으로 안나오는 것
            # IndexError 방지: 1구 콘센트일 경우 
            try:
                curr.remove(list(temp)[0])
            except:
                curr.pop()
            curr.add(appliances[i])
            cnt += 1

    print(cnt)


멀티탭스케줄링()