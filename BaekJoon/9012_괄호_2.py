def 괄호():
    import sys

    def is_VPS(string):
        # 빈 스택
        stack = []

        # 스트링 순회하면서 스택 구성
        for char in string:
            # '('인 경우 stack에 넣는다
            if char == '(':
                stack.append(char)
            # ')'인 경우
            elif not stack: # stack이 비어있을 경우 False
                return "NO"
            else: # '('이면서 비어있지 않은 경우 --> '(' pop
                stack.pop()

        # 순회 마치고 스택이 비어있는지 확인
        if stack:
            return "NO"    # stack에 남아있으면 False
        return "YES"         # stack이 비어있을 때 비로소 VPS


    N = int(sys.stdin.readline())
    answers = [None] * N
    for i in range(N):
        string = sys.stdin.readline().strip()
        answers[i] = is_VPS(string)

    print(*answers, sep='\n')

괄호()