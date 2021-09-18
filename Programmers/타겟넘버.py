def solution(numbers, target):
    
    def _dfs(i):
        
        if i == len(numbers):
            if result[0] == target:
                cnt[0] += 1
            return 
        
        for j in range(2):
            result[0] += numbers[i] * sign[j]
            _dfs(i+1)
            result[0] -= numbers[i] * sign[j]
            