def 막대기1():
    import sys
    input = sys.stdin.readline

    N = int(input())
    stack = []
    # N 개의 숫자를 차례로 받으면서 스택에 쌓아나간다
    for _ in range(N):
        # 현재 입력 숫자
        curr = int(input())

        # 스택은 내림차순을 유지해야 하므로
        # 큰게 나오면 그것보다 작은 막대는 모두 스택에서 제거한다
        while stack and stack[-1] <= curr:
            # stack이 비어있거나, 스택의 마지막이 curr보다 클때가지 계속 뽑는다
            stack.pop()
        
        # 이제 stack[-1] > curr인 상황 --> 스택에 curr 쌓는다
        stack.append(curr)

    # 남은 스택의 개수 출력
    print(len(stack))

def 막대기2():
    import sys
    input = sys.stdin.readline

    # 입력 받기
    N = int(input())
    sticks = [None] * N
    for i in range(N):
        sticks[i] = int(input())
    
    curr = 0 # 현재 보이는 막대기
    cnt = 0  # 보이는 막대기 개수

    # numbers의 마지막부터 거꾸로 순회
    for stick in sticks[::-1]:
        if stick > curr:    # stick이 현재보다 클때만 curr 갱신, cnt++
            cnt += 1
            curr = stick
    
    # 출력
    print(cnt)