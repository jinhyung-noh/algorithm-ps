def solution(n, a, b):

    cnt = 1
    while (abs(a - b) != 1) or ((a + b) % 4 != 3):
        a = (a + 1) // 2
        b = (b + 1) // 2
        cnt += 1

    return cnt


solution(8, 4, 7)