import sys


def bigger_number():

    # inputs
    N, K = list(map(int, sys.stdin.readline().split()))
    number = sys.stdin.readline().strip()
    # N = int('7')
    # K = int('3')
    # number = '1231234'

    stack = []
    idx = 0
    while idx < N and K > 0:
        if not stack:
            stack.append(number[idx])
            idx += 1
            continue
        # 현재 수가 스택 마지막 수보다 크면 스택 마지막이 현재 수보다
        # 작거나 같아질 때까지 뽑는다 --> 이후 계속 진행
        if idx < N and number[idx] > stack[-1]:
            stack.pop()
            K -= 1
            continue
        stack.append(number[idx])
        idx += 1

    # 미처 다 지우지 못한 경우
    if K > 0:
        return "".join(stack[:-K])

    return "".join(stack) + number[idx:]

print(bigger_number())


