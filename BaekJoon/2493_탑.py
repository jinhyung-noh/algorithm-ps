import sys


def towers_():

    # inputs
    N = int(sys.stdin.readline())
    towers = list(map(int, sys.stdin.readline().split()))

    # stack: 다음 것이 더 큰게 나타나기 전까지 기록
    stack = []
    answers = [0] * N

    for i in range(N):
        # stack의 마지막이 현재보다 작거나 같으면 더 큰게 나올때까지 계속 pop
        # while문을 탈출했을때: 1. 빈 스택(왼쪽에 큰 게 없음), 2. stack[-1]이 현재보다 더 큼
        while stack and towers[stack[-1]] <= towers[i]:
            stack.pop()

        if not stack:
            answers[i] = 0
        else:
            answers[i] = stack[-1] + 1
        stack.append(i)

    print(" ".join(map(str, answers)))
    return

towers_()