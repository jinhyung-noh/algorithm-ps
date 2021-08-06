import sys

a, b = sys.stdin.readline().split()

print(max(a[::-1], b[::-1]))