import sys
input = sys.stdin.readline

# inputs
N = int(input())
towers = list(map(int, input().split()))

stack = []
answers = [None] * N

# towers를 인덱스로 순회하면서, 스택과 비교하고 스택 쌓아나간다
for i in range(N):  # i: i번째 인덱스
    # i번째 tower의 높이와 스택에 있는 높이들을 비교한다
    # 스택이 비었거나
    # "스택의 마지막 원소" 번째 tower랑 현재 i번째 tower랑 비교해서 클때까지 뽑는다!
    while stack and towers[stack[-1]] <= towers[i]:
        stack.pop()

    # 여기부터 while문 탈출
    
    if not stack:       # 1) stack이 비었거나
        answers[i] = 0
    else:               # 2) towers[stack[-1]] > towers[i]인 경우
        answers[i] = stack[-1] + 1  # 0 기반 인덱스 아니라 순서로 바꾸어서 저장
    
    # 현재 stack에 넣기: stack에 들어가는 것은 값이 아니라 index
    stack.append(i)

print(*answers)
