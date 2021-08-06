import sys

w, h = map(int, sys.stdin.readline().split())
n = int(input())

hori = []
vert = []

for _ in range(n):
    is_hori, num = map(int, sys.stdin.readline().split())

    if is_hori:
        hori.append(num)
    else:
        vert.append(num)

hori.sort()
hori.append(w)
vert.sort()
vert.append(h)

def get_max_interval(arr):
    before = 0
    max = 0
    for elem in arr:
        if elem - before > max:
            max = elem - before
        before = elem
    return max

print(get_max_interval(hori) * get_max_interval(vert))

