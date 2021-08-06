import sys

max = 0
idx = 0

for i in range(1, 10):
    n = int(sys.stdin.readline())
    if  n > max:
        max = n
        idx = i

print(max)
print(idx)