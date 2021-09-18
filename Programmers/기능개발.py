
def solution(progresses, speeds):
    import math

    answer = []
    N = len(progresses)
    needed_days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(N)]

    max = needed_days[0]
    temp = 1

    for idx in range(1, N):
        if needed_days[idx] > max:
            answer.append(temp)
            max = needed_days[idx]
            temp = 1
            continue
        temp += 1

    # last
    answer.append(temp)

    print(answer)
    return answer 

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]	
solution(progresses, speeds)