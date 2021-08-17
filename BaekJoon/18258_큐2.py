import sys
from collections import deque

def queue():

    def operation(oper: str):
        oper = tuple(oper.split())

        if oper[0] == 'push':
            queue.append(oper[1])
        elif oper[0] == 'pop':
            if len(queue) == 0:
                answers.append(-1)
            else:
                answers.append(queue.popleft())
        elif oper[0] == 'size':
            answers.append(len(queue))
        elif oper[0] == 'empty':
            if len(queue) == 0:
                answers.append(1)
            else:
                answers.append(0)
        elif oper[0] == 'front':
            if len(queue) == 0:
                answers.append(-1)
            else:
                answers.append(queue[0])
        else: # oper[0] == 'back'
            if len(queue) == 0:
                answers.append(-1)
            else:
                answers.append(queue[-1])
        return


    queue = deque()
    answers = []
    # inputs
    N = int(sys.stdin.readline())
    for _ in range(N):
        oper = sys.stdin.readline()
        operation(oper)

    return answers

for answer in queue():
    print(answer)
