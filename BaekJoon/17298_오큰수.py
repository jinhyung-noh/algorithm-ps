import sys

def right_bigger_number():

    # inputs
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    answers = [None] * N
    stack = []
    for i in range(N-1, -1, -1):
        while stack and arr[i] >= arr[stack[-1]]:
            stack.pop()
        
        answers[i] = stack[-1] if stack else -1
        stack.append(i)

    # outputs
    print(" ".join([str(arr[i]) if i != -1 else '-1' for i in answers]))

right_bigger_number()