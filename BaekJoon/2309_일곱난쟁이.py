import sys
import itertools

dwarfs = []
for _ in range(9):
    dwarfs.append(int(sys.stdin.readline()))

dwarfs.sort()
total = sum(dwarfs)

for idx1, idx2 in itertools.combinations(range(9), 2):
    if total - dwarfs[idx1] - dwarfs[idx2] == 100:
        break

for i in range(9):
    if i == idx1 or i == idx2:
        continue
    print(dwarfs[i])
