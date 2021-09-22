def solution(numbers):
    def _conv_num(num):
        if len(num) == 1:
            return num * 4
        if len(num) == 2:
            return num + num[-1] + num[-1]
        if len(num) == 3:
            return num + num[-1]
        else: num

    answer = ''
    idxes = list(range(len(numbers)))

    conv_numbers = [_conv_num(num) for num in map(str, numbers)]

    sorted_nums = sorted(zip(conv_numbers, idxes), key=lambda x: x[0], reverse=True)
    for num, idx in sorted_nums:
        answer += str(numbers[idx])
    return answer

numbers = [6, 10, 2]
print(solution(numbers))
