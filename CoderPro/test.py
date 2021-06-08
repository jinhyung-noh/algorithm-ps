def solution(array, commands):
    def function1(array, cmd): 
        """
        input	: 1x3 array [x, x, x]
        return	: integer
        """
        result = sorted(array[cmd[0]-1:cmd[1]])
        return result[cmd[2]-1]
    answer = []
    for cmd in commands:
        answer.append(function1(array, cmd))
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))