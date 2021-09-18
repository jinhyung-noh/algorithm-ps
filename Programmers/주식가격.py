def solution(prices):
    N = len(prices)
    result = [0] * N
    stack = []
    
    # append stack if prices[curr] is greater or equal than prices[stack[-1]]
    # index is stored in stack
    for curr in range(N):
        while stack and prices[stack[-1]] > prices[curr]:
            prev = stack.pop()
            result[prev] = curr - prev
        stack.append(curr)
    
    # final check
    while stack:
        prev = stack.pop()
        result[prev] = (N - 1) - prev
    
    return result