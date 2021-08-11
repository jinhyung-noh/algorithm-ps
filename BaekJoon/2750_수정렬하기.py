import sys
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
arr = [0] * n
for i in range(n):
    arr[i] = int(sys.stdin.readline())

def quick_sort(seq):
    if len(seq) <= 1:
        return seq

    pivot = seq[0]
    remaining = seq[1:]
    left_part = [x for x in remaining if x<= pivot]
    right_part = [x for x in remaining if x> pivot]
    return quick_sort(left_part) + [pivot] + quick_sort(right_part)

for num in quick_sort(arr):
    print(num)
