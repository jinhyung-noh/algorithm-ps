import sys

x = int(sys.stdin.readline().split()[-1])
nums = [int(i) for i in sys.stdin.readline().split()]

cnt = 0

for num in nums:
    if num < x:
        print(num, end=" ")

