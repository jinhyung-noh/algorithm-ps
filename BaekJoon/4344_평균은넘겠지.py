import sys

n = int(input())
answers = []
for _ in range(n):
    scores = [int(i) for i in sys.stdin.readline().split()][1:]

    mean = sum(scores) / len(scores)
    cnt = 0
    for score in scores:
        if score > mean:
            cnt += 1

    answers.append(cnt / len(scores) * 100)

for answer in answers:
    print(f"{answer:.3f}%")