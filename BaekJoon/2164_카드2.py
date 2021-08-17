import sys

def last_card():

    # inputs
    N = int(sys.stdin.readline())
    arr = range(1, N+1)
    while len(arr) > 1:
        arr = [arr[2*i+1] for i in range(N // 2)]
        if N % 2 == 1:
            arr = arr[1:] + [arr[0]]
        N //= 2

    print(arr[0])

last_card()
