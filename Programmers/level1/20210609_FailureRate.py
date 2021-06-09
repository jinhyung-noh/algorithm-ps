def solution(N, stages):

    hashmap = {}
    for i in range(1, N+2):
        hashmap[i] = stages.count(i)
    
    for num in stages:
        if num not in hashmap:
            hashmap[num] = 0
        else:
            hashmap[num] += 0
    for i in range(0, N+2):
        if i not in hashmap:
            hashmap[i] = -1
            
    failure_list = []
    for num in range(N, 0, -1):
        try:
            failureRate = hashmap[num] / sum([hashmap[i] for i in range(N+1, num-1, -1)])
        except:
            failureRate = 0
        failure_list.append((num, failureRate))
    
    failure_list.sort(key=lambda x: (x[1], -x[0]), reverse=True)

    return [i[0] for i in failure_list]


N = 4
stages = [1,2,3,3,2,2]
print(solution(N, stages))

    