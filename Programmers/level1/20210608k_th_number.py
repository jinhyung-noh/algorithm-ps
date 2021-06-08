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
