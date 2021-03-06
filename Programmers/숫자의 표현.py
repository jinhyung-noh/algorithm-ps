def solution(n):
    cnt = 0
    # 홀수개의 합
    for k in range(1, n, 2):
        center = n/k
        # 중심이 정수이고, 맨 왼쪽수가 0보다 클때
        if (center % 1  == 0) and (center - k//2 > 0):
            cnt += 1

    # 짝수개의 합
    for k in range(2, n, 2):
        center = n/k
        # 중심이 xx.5이고, 맨 왼쪽수가 0보다 클때
        if (center % 1 == 0.5) and (center + 0.5 - k//2 > 0):
            cnt += 1

    return cnt
n = 15
print(solution(n))
