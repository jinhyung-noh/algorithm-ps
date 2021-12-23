numbers = [5,0,2,7]	

def solution(numbers):
    answer = []
    N = len(numbers)
    for i in range(N):
        for j in range(i+1, N):
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer

print(solution(numbers))