import sys


def plus_cycle(n: int):
    original = n
    cnt = 0

    while True:
        cnt += 1
        if n < 10:
            n = 10 * n + n
        else:
            one_digit = n % 10
            ten_digit = n // 10
            n = 10 * one_digit + (ten_digit + one_digit) % 10
        # check 
        if n == original:
            break
    return cnt

n = int(sys.stdin.readline())
print(plus_cycle(n))