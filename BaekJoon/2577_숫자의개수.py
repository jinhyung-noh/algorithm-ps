import sys
from collections import Counter

target = 1
for _ in range(3):
    target *= int(sys.stdin.readline())

hash = Counter(list(str(target)))

for i in range(10):
    print(hash[str(i)])
