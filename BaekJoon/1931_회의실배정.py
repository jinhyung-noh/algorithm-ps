import sys


def 회의실배정():
    # inputs
    N = int(sys.stdin.readline())
    meetings = [None] * N
    for i in range(N):
        meetings[i] = tuple(map(int, sys.stdin.readline().split()))

    # sort meetings
    # first criteria: end time increasing order
    # second criteria: strat time increasing order
    meetings.sort(key=lambda x: (x[1], x[0]))

    cnt = 0
    end = 0
    for meeting in meetings:
        # 다음 미팅시간이 현재 끝시간 이상이면 추가
        if meeting[0] >= end:
            cnt += 1
            end = meeting[1]

    print(cnt)
    return

회의실배정()
