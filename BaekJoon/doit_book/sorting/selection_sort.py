from typing import MutableSequence
import sys

def selection_sort(arr: MutableSequence) -> None:
    n = len(arr)

    # index 0 to i-1 is sorted
    for i in range(n-1):        # last arr[n-1] is unnecessray
        min_idx = i
        # find index of mininum (i .. n-1)
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # swap arr[i] and arr[idx]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

a = list(range(9,-1,-1))
print(a)
selection_sort(a)
print(a)
        
