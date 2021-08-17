import sys


def circle_area():

    # inputs
    N = int(sys.stdin.readline())
    points = [None] * (2 * N)
    for i in range(N):
        center, radius = list(map(int, sys.stdin.readline().split()))
        points[2*i] = (center - radius, 'l')        # left point
        points[2*i+1] = (center + radius, 'r')      # right point

    # sort points: x-coordinates in ascending order
    #              'l', 'r': decending order ; 'r', 'l' order
    points.sort(key=lambda x: (-x[0], x[1]), reverse=True)

    # count closed area
    cnt = 0
    stack = []
    for i in range(2 * N):
        # (a, 'r') (b, 'r') r, r연속으로 나왔을 때 연결 여부 탐색 시작 --> l, l 연속으로 나올 때까지
        if points[i][1] =='r' and stack[-1][1] == 'r':
            is_connected = True
            curr = stack.pop()

            # 처음이 끊어졌는지 확인
            if points[i][0] != curr[0]:
                is_connected = False

            # (a, 'l') (b, 'l') l,l연속으로 나올 때까지 pop하면서 연결 여부 파악
            while not(curr[1] == 'l' and stack[-1][1]  == 'l'):
                if curr[1] == 'l' and curr[0] != stack[-1][0]:
                    is_connected = False
                curr = stack.pop()

            # 마지막이 끊어졌는지 확인
            if curr[1] == 'l' and curr[0] != stack[-1][0]:
                is_connected = False

            # 탐색 종료시 연결되었으면 cnt++
            if is_connected:
                cnt += 1

        stack.append(points[i])

    return N + 1 + cnt



print(circle_area())