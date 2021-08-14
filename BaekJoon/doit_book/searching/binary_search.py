import sys

def binary_search(arr: list, target: int):
    """return index of target or -1"""

    def _binary_search_helper(left: int, right: int):
        # base case 1
        if left > right:
            return -1
        
        center = (left + right) // 2
        # base case2
        if arr[center] == target:
            return center

        # recursive call
        if arr[center] < target:
            return _binary_search_helper(center+1, right)
        else:
            return _binary_search_helper(left, center - 1)

    return _binary_search_helper(0, len(arr) -1)

arr = list(range(1, 20, 2))

print(binary_search(arr, 4))


