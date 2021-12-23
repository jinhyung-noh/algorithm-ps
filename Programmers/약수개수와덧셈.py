left = 13
right = 17

def solution(left, right):
    result = 0
    # left ~ right 범위 내 숫자들 순회
    for i in range(left, right+1):
        # 범위 내 숫자가 제곱수인지 여부 확인
        tmp = i ** (1/2)
        if tmp % 1 == 0:
            # 제곱수일 경우 빼기
            result -= i
            continue   
        # 제곱수가 아닐 경우 더하기
        result += i
    return result


print(solution(left, right))