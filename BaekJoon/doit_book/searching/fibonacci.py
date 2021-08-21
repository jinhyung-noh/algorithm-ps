import sys

def fib(n: int):

    
    stack = [n]
    result = 0

    while stack:
        num = stack.pop()
        if num == 1 or num == 2:
            result += 1
            continue
        stack.append(num - 2)
        stack.append(num - 1)

    return result

for i in range(1, 10):
    print(f'fib({i}) is: {fib(i)}')