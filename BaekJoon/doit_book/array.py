import sys
from typing import Any, MutableSequence, Sequence

def card_conv(x: int, r: int) -> str:
    """return r based string or integer x"""

    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x = x // r

    return d[::-1]

def reverse_array(a: MutableSequence) -> None:
    """reverse the mutable sequence a"""
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-1-i] = a[n-1-i], a[i]
        
def max_of(a: Sequence) -> Any:
    """시퀀스형 a원소의 최댓값을 반환"""
    max =a[0]

    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]
    return max


if __name__ == '__main__':
    print('원소 수를 입력하세요: ', end="")
    num = int(sys.stdin.readline())

    arr = [None] * num

    for i in range(num):
        print(f'{i}번째 원소를 입력하세요: ', end="")
        arr[i] = int(sys.stdin.readline())

    print(arr)
