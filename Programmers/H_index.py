def solution(citations):
    citations.sort(reverse=True)
    
    answer = 0
    for i in range(len(citations)):
        answer = max(answer, min([i+1, citations[i]]))
        
    return answer