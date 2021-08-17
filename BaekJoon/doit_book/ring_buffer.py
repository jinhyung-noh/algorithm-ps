import sys

n = int(sys.stdin.readline())
a = [None] * n

cnt = 0
while True:
    print(f'{cnt+1}번째 정수를 입력하세요: ', end='')
    a[cnt % n] = int(sys.stdin.readline())
    cnt += 1


    print(f'계속 할까요?(Y/ N)', end='')
    retry = sys.stdin.readline().strip()
    if retry in 'Nn':
        break

i = cnt - n
if i < 0: i=0

while i < cnt:
    print(f'{i+1}번째 = {a[i % n]}')
    i += 1