import sys

string = sys.stdin.readline().strip()

stack = []
# 답: 관통수 + 막대수
cnt_lazer = 0   # 관통수
cnt_stick = 0   # 원래 막대 수
before = ""     # ')' 나왔을 때: 레이저인지, 막대 끝인지 구분하기 위해 이전 것 기록

# string = "()(((()())(())()))(())"
for char in string:

    if char == '(':
        stack.append(char)
        before = char
        continue

    # 여기부터는 char == ')'
    # 레이저인지, 막대 끝인지 구분해야한다
    stack.pop()

    if before == '(': # 레이저
        cnt_lazer += len(stack)
    
    else:             # 막대 끝
        cnt_stick += 1
    
    before = char

print(cnt_lazer + cnt_stick)

