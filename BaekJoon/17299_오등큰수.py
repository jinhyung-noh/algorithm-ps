import sys
from collections import Counter

def ngf():

    # inputs
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    counts = Counter(arr)
    F_arr = [(counts[arr[i]], i) for i in range(N)]

    answers = [None] * N
    stack = []
    for i in range(N-1, -1, -1):
        while stack and F_arr[i][0] >= stack[-1][0]:
            stack.pop()
        
        answers[i] = stack[-1][1] if stack else -1
        stack.append(F_arr[i])

    # outputs
    print(" ".join([str(arr[i]) if i != -1 else '-1' for i in answers]))

ngf()
