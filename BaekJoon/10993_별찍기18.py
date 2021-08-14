import sys

def print_triange():

    def _make_triangle(n: int):
        """make arr to triange"""
        center = 2 ** n - 1
        bottom = 1 if n % 2 == 0 else center
        while n > 0:
            num = 2 ** n - 1
            for i in range(0, num):
                arr[bottom-1][center-i-1] = arr[bottom-1][center+i-1] \
                    = arr[bottom + (-1)**n*i-1][center-(num-1-i)-1] \
                    = arr[bottom + (-1)**n*i-1][center+(num-1-i)-1] = "*"
            n -= 1
            bottom = bottom + (-1)**(n+1) * (2**n - 1)
        return 

    n = int(sys.stdin.readline())
    arr = [[" "] * (2**(n+1)-3) for _ in range(2**n-1)]
    _make_triangle(n)

    for i in range(len(arr)):
        print("".join(arr[i]).rstrip())

print_triange()
