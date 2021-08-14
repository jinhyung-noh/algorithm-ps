import sys

A, B, C = list(map(int, sys.stdin.readline().split()))

B = bin(B)
A = A % C
answer = 1
for bit in B[2:]:
    answer = (answer ** 2) * (A ** int(bit))
    answer = answer % C

print(answer)