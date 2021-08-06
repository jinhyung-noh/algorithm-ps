import sys

n = int(input())
cases = [sys.stdin.readline().split() for _ in range(n)]

for each_case in cases:
    print(int(each_case[0])+int(each_case[1]))