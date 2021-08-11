from typing import MutableSequence

def insertion_sort(arr: MutableSequence) -> None:

    n = len(arr)
    for i in range(1, n):
        while i >= 0 and arr[i] < arr[i-1]:
            # swap
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1

a = list(range(9, -1, -1))
print(a)
insertion_sort(a)
print(a)