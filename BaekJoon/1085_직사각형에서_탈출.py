import sys

x, y, w, h =  [int(i) for i in sys.stdin.readline().split()]

print(min(x, w-x, y, h-y))