import sys

N, r, c = map(int, sys.stdin.readline().split())

def bisect(x, N):
    if x < 2**(N-1):
        return 0, x
    return 1, x - 2**(N-1)

def quadrant(x_bisect, y_bisect):
    if (x_bisect, y_bisect) == (0, 0):
        return 0
    elif (x_bisect, y_bisect) == (0, 1):
        return 1
    elif (x_bisect, y_bisect) == (1, 0):
        return 2
    else:
        return 3
        
def z_func(N, r, c):

    # base case
    if N == 0:
        return 0

    # recursive call
    bisect_r, new_r = bisect(r, N)
    bisect_c, new_c = bisect(c, N)
    return 2**(2*(N-1)) * quadrant(bisect_r, bisect_c) + z_func(N-1, new_r, new_c)

print(z_func(N, r, c))