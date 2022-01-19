def solution(s):

    status = 0
    for char in s:
        if char == '(':
            status += 1
        else:
            status -= 1

        # 확인 1: 짝이 맞지 않는 ')'
        if status < 0:
            return False
    # 확인 2: 순회를 마치고 남은'('
    if status > 0:
        return False
    # 다 통과하면 True
    return True

s = "(()("
print(solution(s))