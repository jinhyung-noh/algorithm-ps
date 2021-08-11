import sys
import itertools

N = int(input())
nums = [int(i) for i in sys.stdin.readline().split()]

max = 0
for perm in itertools.permutations(range(N)):

    sum = 0
    for j in range(1, N):
        sum += abs(nums[perm[j]] - nums[perm[j-1]])

    if sum > max:
        max = sum

print(max)



