import sys


def fib(n: int):

    def _fib_helper(i: int):

        # base case
        if i == 1 or i == 2:
            return 1

        # using cache
        if cache[i]:
            return cache[i]
        
        # recursive call
        cache[i] = _fib_helper(i-1) + _fib_helper(i-2)
        return cache[i]

    cache = [0] * (n +1)
    return _fib_helper(n)

# inputs
N = int(sys.stdin.readline())

print(fib(N))