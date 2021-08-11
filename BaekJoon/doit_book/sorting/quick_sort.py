from typing import MutableSequence


def quick_sort(arr: MutableSequence, start: int, end: int):

    if start >= end:        # 원소 1개 종료
        return

    pivot = start           # pivot은 첫번째 원소
    left = start + 1
    right = end
    while left <= right:
        # move -> until bigger than piivot
        while left <= end and arr[left] <= arr[pivot]: left += 1
        # move <- until smaller than piivot
        while right > start and arr[right] >= arr[pivot]: right -= 1
        # crossed --> swap pivot and small(right)
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # not crossed --> swap arr[left] and arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

    # after dividing --> sort left part and right part recursively
    quick_sort(arr, start, right)
    quick_sort(arr, left, end)


def quick_sort2(arr: MutableSequence) -> list:
    # terminate if arr has equal or less than 1 element
    if len(arr) <= 1 :
        return arr

    pivot = arr[0]      # pivot: first element
    tail = arr[1:]      # arr exccept pivot(first element)

    left_side = [x for x in tail if x <= pivot] 
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

arr = list(range(20, -1, -1))
print(arr)
# quick_sort(arr, 0, len(arr)-1)
print(quick_sort2(arr))


        

