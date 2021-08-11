import sys

n = int(sys.stdin.readline())
Array = [0] * 10001

for _ in range(n):
    Array[int(sys.stdin.readline())] += 1
    
for i in range(10001):
    for _ in range(Array[i]):
        print(i)