import sys


def stack_():

    def _stack_operation(order: str):
        if order[0] == 'push':
            stack.append(order[1])

        elif order[0] == 'pop':
            if len(stack) == 0:
                answers.append(-1)
            else:
                answers.append(stack.pop())

        elif order[0] == 'size':
            answers.append(len(stack))

        elif order[0] == 'empty':
            if len(stack) == 0:
                answers.append(1)
            else:
                answers.append(0)
        else:           # top
            if len(stack) == 0:
                answers.append(-1)
            else:
                answers.append(stack[-1])



    stack = []
    answers = []

    # inputs
    N = int(sys.stdin.readline())
    for _ in range(N):
        order = sys.stdin.readline().split()
        _stack_operation(order)
        
    for answer in answers:
        print(answer)

stack_()