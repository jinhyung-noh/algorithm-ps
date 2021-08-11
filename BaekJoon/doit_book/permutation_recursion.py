import sys


arr = [0, 1, 2, 3, 4]

def permute(arr: list, l: int, r: int):
    # base case
    if l == r:
        print(arr)
        return
    
    # recursive call
    for i in range(l, r+1):
        # swapping
        arr[i], arr[l] = arr[l], arr[i]

        permute(arr, l+1, r)

        # backtracking
        arr[i], arr[l] = arr[l], arr[i]


def permute2(l: int, r: int):
    global arr
    # base case
    if l == r:
        print(arr)
        return
    
    # recursive call
    for i in range(l, r+1):
        # swapping
        arr[i], arr[l] = arr[l], arr[i]

        permute2(l+1, r)

        # backtracking
        arr[i], arr[l] = arr[l], arr[i]
permute2(0, len(arr)-1)