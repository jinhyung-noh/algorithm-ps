import sys

answers = []

n = int(input())
for _ in range(n):
    problems = sys.stdin.readline().strip()
    total_score = 0
    each_score = 0
    
    for problem in problems:
        if problem == 'X':
            each_score = 0
        else:
            each_score += 1
            total_score += each_score
    
    answers.append(total_score)

for answer in answers:
    print(answer)