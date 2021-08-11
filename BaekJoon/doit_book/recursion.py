from collections import deque

def recur(n):
    s = deque()

    while True:
        if n > 0:
            s.append(n)
            n = n - 1
            continue
        if s:
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break

def recur2(n):
    s = deque()

    while True:
        if n > 0:
            s.append(n)
            n = n - 2
            continue
        if s:
            n = s.pop()
            print(n)
            n = n - 1
            continue
        break

recur(4)
print("========================")
recur2(4)
