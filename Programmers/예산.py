d = [1,3,2,5,4]
budget = 9

def solution(d, budget):
    result = 0
    d.sort()
    # if budget < d[0]:
    #     return 0
    # if budget >= sum(d):
    #     return len(d)
    else: 
        check_sum = 0
        for case in d:
            if check_sum <= budget:
                check_sum += case
                result += 1
    return result - 1

print(solution(d, budget))