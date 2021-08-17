import sys

def is_VPS(string: str):

    cnt = 0 
    for char in string:
        if char == '(':
            cnt += 1
        else:
            cnt -= 1
        # check
        if cnt < 0:
            return 0

    
    if cnt == 0:        # VPS
        return 1
    return 0            # not VPS


# input
N = int(sys.stdin.readline())
answers = [None] * N
for i in range(N):
    answers[i] = is_VPS(sys.stdin.readline().strip())

# print
for answer in answers:
    if answer:
        print("YES")
    else:
        print("NO")