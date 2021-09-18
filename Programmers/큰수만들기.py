def solution(number, k):

    stack = []

    i = 0
    for num in number:
        if k == 0:
            break
        while (stack and  k > 0 and stack[-1] < num):
            stack.pop()
            k -= 1
        stack.append(num)
        i += 1
    
    
    stack += number[i:]
    # 나머지 처리
    if (k > 0):
        stack = stack[:-k]
        
    return ''.join(stack)

print(solution("4177252841", 3))
