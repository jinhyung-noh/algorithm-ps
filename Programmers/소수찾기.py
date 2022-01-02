def solution(s):
    from math import sqrt, floor

    def _is_prime(n):
        # 소수인지 판별하는 함수
        if n <= 1:
            return False
        if n == 2:
            return True

        if n % 2 == 0:
            return False
        for i in range(3, floor(sqrt(n))+1, 2):
            if n % i == 0:
                return False
        return True

    def _permutation():

        # 해당 idx의 수들을 합쳤을때 primes에 없고, 소수이면 추가
        temp = int(''.join([ s[i] for i in idx_permutaion]))
        if temp not in primes and _is_prime(temp):
            primes.add(temp)
        
        # recursive call: 다음 permutation
        for next_idx in range(N):
            # 사용 안 된 경우만 고려
            if not idx_used[next_idx]:
                idx_used[next_idx] = True
                idx_permutaion.append(next_idx)
                _permutation()
                idx_permutaion.pop()
                idx_used[next_idx] = False

    ####### main function ####### 
    N = len(s)
    idx_used = [False] * N  # idx가 사용되었는지 여부 기록, recursion 들어갈때마다 확인하는 용도
    idx_permutaion = [] # idx들의 순열들
    primes = set()

    for start in range(N):
        idx_used[start] = True      # idx 사용 기록
        idx_permutaion.append(start)# permutation에 추가
        _permutation()              # next permuation
        idx_permutaion.pop()        # 빠져나오면 해당 idx 제거
        idx_used[start] = False     # idx 사용 기록 제거

    return len(primes)

s = "4"
print(solution(s))