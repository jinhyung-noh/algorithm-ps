import sys

def func():

    # inputs
    string = sys.stdin.readline().strip()
    string = '(' + string + ')'

    stack = []
    for i in range(len(string)):
        if string[i] == ')':
            temp = []
            while stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()     # remove '(' 
            stack.append("".join([temp[2], temp[0], temp[1]]))
        else:
            stack.append(string[i])

    print(stack[0])

func()
