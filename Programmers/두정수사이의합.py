def solution(a, b):
    a, b = min(a, b), max(a, b)

    return (a + b) * (b - a + 1) // 2