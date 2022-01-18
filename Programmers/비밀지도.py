def solution(n, arr1, arr2):

    def _helper(n, k):
        # k를 "#", " "의 스트링으로 변환
        result = ""
        while n > 0:
            if k % 2 == 0:
                result += " " 
            else:
                result += "#"
            k //= 2
            n -= 1
        return result[::-1]

    answer = [None] * n
    for i in range(n):
        answer[i] = _helper(n, arr1[i] | arr2[i])
    return answer

n = 6
arr1 =[46, 33, 33 ,22, 31, 50] 
arr2 = [27 ,56, 19, 14, 14, 10]

print(solution(n, arr1, arr2))