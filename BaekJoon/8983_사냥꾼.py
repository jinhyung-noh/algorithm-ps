import sys
from bisect import bisect_left, bisect_right

def huntable_animals():

    # input
    M, N, L = list(map(int, sys.stdin.readline().split()))
    shootpoints = list(map(int, sys.stdin.readline().split()))
    animals = [None] * N
    for i in range(N):
        animals[i] = tuple(map(int, sys.stdin.readline().split()))

    # sort shootpoints
    shootpoints.sort()

    # count hauntable animals
    cnt = 0
    for x_ani, y_ani in animals:
        left = bisect_left(shootpoints, x_ani+y_ani-L)
        right = bisect_right(shootpoints, x_ani-y_ani+L)
        # right - left: number of hauntable shootpoints of the animal
        if right - left > 0:
            cnt += 1

    return cnt

print(huntable_animals())
