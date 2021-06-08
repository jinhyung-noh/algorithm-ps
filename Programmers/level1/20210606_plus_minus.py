def solution(absolutes, signs):
    length = len(absolutes)
    result = 0
    for i in range(length):
        sign = 1
        if not signs[i] :
            sign = -1
        result += sign * absolutes[i]
    return result
