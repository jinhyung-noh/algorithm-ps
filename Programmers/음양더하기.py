def solution(absolutes, signs):
    N = len(absolutes)
    total = 0
    for i in range(N):
        sign = 1 if signs[i] else -1
        total += absolutes[i] * sign
    return total