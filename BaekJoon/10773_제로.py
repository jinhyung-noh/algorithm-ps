import sys

def zero():


    # input
    N = int(sys.stdin.readline())
    stack = [0] * N
    ptr = 1
    for _ in range(N):
        n = int(sys.stdin.readline())
        if n == 0:
            ptr -= 1
        else:
            stack[ptr-1] = n
            ptr += 1

    return sum(stack[:ptr-1])

print(zero())

    
