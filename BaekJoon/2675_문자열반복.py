import sys

n = int(input())
answers = []

for _ in range(n):
    repeat, seq = sys.stdin.readline().split()

    res = ""
    for char in seq:
        for _ in range(int(repeat)):
            res += char
    
    answers.append(res)

for answer in answers:
    print(answer)