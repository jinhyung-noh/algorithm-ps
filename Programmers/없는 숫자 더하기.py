numbers = [1,2,3,4,6,7,8,0]	

def solution(numbers):
    result = 0
    for i in range(100):
        result += i
    return result - sum(numbers)

print(solution(numbers))