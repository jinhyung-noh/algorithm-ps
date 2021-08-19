import sys

def iron_rod():

    # input 
    string = sys.stdin.readline().strip()

    result = 0
    cnt_left = 0
    stack = []

    for char in string:

        if char == '(':
            stack.append(char)
            cnt_left += 1

        else:   # ')'
            if stack[-1] =='(':
                stack.pop()
                cnt_left -= 1
                stack.append(cnt_left)
            else: # number
                cnt = 0
                temp_stack = []
                while stack[-1] != '(':
                    cnt += 1
                    num = stack.pop()
                    if num > 1:
                        temp_stack.append(num - 1)
                stack.pop() # '(' 제거
                cnt_left -= 1
                stack = stack + temp_stack[::-1]
                result += (cnt + 1)
    return result

print(iron_rod())

