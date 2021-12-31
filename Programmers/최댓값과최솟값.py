def solution(s):
    from sys import maxsize

    numbers = map(int, s.split(" "))
    max_num = -maxsize
    min_num = maxsize

    # numbers 순회하면서 min, max 갱신
    for number in numbers:
        max_num = max(max_num, number)
        min_num = min(min_num, number)

    return str(min_num) + str(max_num)

s = "-1 -2 -3 -4"
print(solution(s))