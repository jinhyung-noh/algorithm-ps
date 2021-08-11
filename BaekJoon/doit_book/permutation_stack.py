import sys

print("Enter a integer: ", end="")
n = int(sys.stdin.readline())

result = []
stack = list(map(str, range(1, n+1)))[::-1]
print(stack)
print("########################")

while stack:
    s = stack.pop()

    if len(s) == n:
        result.append(s)
        continue
    
    for i in range(n, 0, -1):
        if str(i) in s:
            continue
        stack.append(s+str(i))

print(f"The permutation of {n} is below\n####################")
print(result)
