def theGameOfDeath():
    import sys
    T = int(sys.stdin.readline())

    answers = []
    # 각 case마다 반복: T번
    for _ in range(T):
        N = int(sys.stdin.readline())
        # 인접리스트 구성
        people = {}
        for i in range(1, N+1):
            people[i] = int(sys.stdin.readline())

        cnt = 1     # 횟수
        curr = 1    # 현재 사람
        while (cnt <= N) and (people[curr] != N):
            cnt += 1                # 횟수++
            curr = people[curr]     # 다음 사람 지목

        # 불가능 케이스인지 확인
        if cnt > N:
            cnt = 0
        answers.append(cnt)
    
    # 출력
    print(*answers, sep='\n');

theGameOfDeath()

    

