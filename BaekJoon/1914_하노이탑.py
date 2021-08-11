import sys

N = int(sys.stdin.readline())

def hanoi(n, start, stop) -> int:
    # base case
    if n < 1:
        return 
    
    # recursive call
    hanoi(n-1, start, 6-start-stop)
    print(start, stop)
    hanoi(n-1, 6-start-stop, stop)


print(2**N-1)
if N <= 20:
    hanoi(N, 1, 3)
