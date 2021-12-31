def solution(n):
    from math import sqrt, trunc
    total = 0
    square_root = sqrt(n)
    # sqrt(n)까지 순회하면서 나누어떨어지면 추가
    for i in range(1, trunc(square_root)+1):
        if n % i == 0:
            total += i
            total += (n//i)
    
    # 제곱수일 경우 두번 추가되었으므로 빼준다
    if square_root % 1 == 0:
        total -= square_root

    return total

n=5
print(solution(n))

