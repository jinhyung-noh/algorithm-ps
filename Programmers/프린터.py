def solution(priorities, location):
    from collections import deque
    priorities = deque(priorities)

    target_index = location
    answer = 0
    while priorities:
        x = priorities.popleft()
        if x >= max(priorities):
            answer += 1
            # 출력한 대상이 target인 경우
            if target_index == 0:
                return answer
            # 출력한 대상이 target이 아닌 경우
            else:    
                target_index -= 1
        else:
            priorities.append(x)
            if target_index == 0:
                target_index = len(priorities)-1
            else:
                target_index -= 1

priorities = [1]
location = 0
print(solution(priorities, location))