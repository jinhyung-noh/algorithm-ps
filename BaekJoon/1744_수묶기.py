def 수묶기():
    import sys
    input = sys.stdin.readline

    N = int(input())
    numbers = [0] * N
    for i in range(N):
        numbers[i] = int(input())

    # DESC sort
    numbers.sort(reverse=True)

    idx = 0
    total = 0
    # 양수부분 묶기
    while idx+1 < len(numbers) and numbers[idx] > 1 and numbers[idx+1] > 1:
        total += numbers[idx] * numbers[idx+1]
        idx += 2

    idx_rev = N-1
    # 음수부분 묶기
    while idx_rev-1 >= 0 and numbers[idx_rev] < 0 and numbers[idx_rev-1] <= 0:
        total += numbers[idx_rev] * numbers[idx_rev-1]
        idx_rev -= 2

    # 중간부분 처리
    total += sum(numbers[idx:idx_rev+1])

    print(total)

    
수묶기()