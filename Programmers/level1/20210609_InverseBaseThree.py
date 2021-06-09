def solution(n):
    result=[]
    while n>0:
        result.insert(0, n % 3)
        n = n // 3
    return sum([result[i] * 3**i for i in range(len(result))])

print(solution(25))